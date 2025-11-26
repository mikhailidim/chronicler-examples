import os
from flask import Flask, render_template, request, session
from flask_session import Session
from dotenv import load_dotenv
from clerk_backend_api import Clerk
from clerk_backend_api.security.types import AuthenticateRequestOptions, AuthStatus
import logging
import jwt

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SESSION_SECRET')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

origins = ['http://127.0.0.1:5001',
            os.getenv('APP_URL', 'http://localhost:5001')]

clerk_client = Clerk(bearer_auth=os.getenv('CLERK_SECRET_KEY'),
            debug_logger=logging.getLogger("clerk:api"))

def get_user_subscription(userid):
    """
    Retrieves the billing subscription information for a specific user from Clerk.
    Fetches the user's subscription details and formats them into a dictionary.
    Returns subscription data including user ID, plan status, and plan name if available.
    Returns None if the user has no active subscription.
    """
    res = clerk_client.users.get_billing_subscription(user_id=userid)
    if res is not None:
        logging.debug(f" User {userid} subscribed to {res}")
        return  {"sub": userid, "plan_status": res.status.value,"plan": res.subscription_items[0].plan.name}
    else:
        return None

def check_clerk_handshake(request):
    """
    Checks for and processes Clerk handshake tokens from request query parameters.
    Decodes the JWT handshake token without signature verification to extract cookie data.
    Returns a list of cookies needed for Clerk authentication if handshake is present.
    Returns None if no handshake token is found or if decoding fails.
    """
    try:
        # Check query parameters
        handshake_token = request.args.get("__clerk_handshake") 
        if handshake_token:
            logger.debug(f"Clerk handshake token from query params: {handshake_token}")       
            decoded = jwt.decode(handshake_token.encode('utf-8'), options={"verify_signature": False})
            logger.debug(f"Clerk handshake decoded: {decoded}")
            if isinstance(decoded, dict) and isinstance(decoded.get("handshake"), list):
                handshake_list = decoded.get("handshake")
            elif isinstance(decoded, list):
                handshake_list = decoded
                logger.debug("Clerk handshake cookies set in request")
            return handshake_list    
    except jwt.DecodeError as e:
        logger.error(f"Failed to decode clerk handshake token: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Error handling clerk handshake: {str(e)}")
        return None

@app.before_request
def request_clerk_state():
    """
    Executes before each request to authenticate users with Clerk.
    Processes Clerk handshake cookies if present and modifies the request environment.
    Authenticates the request using the Clerk API and stores the authentication state in the session.
    Handles authentication errors gracefully by logging them without blocking the request.
    """
    _clerk_cookies = check_clerk_handshake(request)
    logging.debug(f"Clerk cookies from handshake: {_clerk_cookies}")
    if _clerk_cookies:
        request.environ['HTTP_COOKIE'] = '; '.join(_clerk_cookies)
        logging.debug(f"Modified request for Clerk: {request}")  
    try:
        # Authenticate the request with Clerk
        _request_state = clerk_client.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=origins
            )
        )
        logger.debug(f"Authentication state: {_request_state.is_authenticated}, Payload: {_request_state.payload}")
        session['clerk_state'] = _request_state
        _sub_stat = get_user_subscription(_request_state.payload['sub']) if _request_state.payload else None
        logging.debug(f" Subscription status is {_sub_stat}")
        session['subs'] = _sub_stat
    except Exception as e:
        logger.error(f"Error during Clerk authentication: {e}")

@app.route('/')
def index():
    """
    Renders the home page of the application.
    Retrieves the Clerk authentication state from the session and passes it to the template.
    Provides the Clerk publishable key for client-side authentication.
    """
    _cs = session.get('clerk_state')
    _pl = session.get('subs')
    logger.debug(f"Rendering plans page with clerk state: {_cs} and plan {_pl}")
    return render_template('index.html',
                        clerk_publishable_key=os.getenv('CLERK_PUBLISHABLE_KEY'),
                        is_authenticated=_cs.status == AuthStatus.SIGNED_IN if _cs else False,
                        clerk_state=_cs,
                        clerk_plan=_pl)

@app.route('/plans')
def plans():
    """
    Renders the plans page where users can view available subscription plans.
    Retrieves the Clerk authentication state from the session to determine user access.
    Passes authentication context to the template for conditional rendering.
    """
    _cs = session.get('clerk_state')
    logger.debug(f"Rendering plans page with clerk state: {_cs}")
    return render_template('plans.html',
                        clerk_publishable_key=os.getenv('CLERK_PUBLISHABLE_KEY'),
                        is_authenticated=_cs.status == AuthStatus.SIGNED_IN if _cs else False,
                        clerk_state=_cs)


@app.route('/profile')
def profile():
    """
    Renders the user profile page.
    Retrieves the Clerk authentication state from the session to display user information.
    Provides authentication context for personalizing the profile view.
    """
    _cs = session.get('clerk_state')
    logger.debug(f"Rendering plans page with clerk state: {_cs}")
    return render_template('profile.html',
                        clerk_publishable_key=os.getenv('CLERK_PUBLISHABLE_KEY'),
                        is_authenticated=_cs.status == AuthStatus.SIGNED_IN if _cs else False,
                        clerk_state=_cs)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
