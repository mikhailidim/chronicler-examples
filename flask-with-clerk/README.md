# Flask with Clerk Authentication


A Flask web application demonstrating integration with [Clerk](https://clerk.com) for user authentication and session management. This example shows how to implement secure authentication in a Flask application using Clerk's Backend API and client-side components.


## Overview

This application provides a complete authentication flow including:

- User sign-in and sign-up using Clerk
- Session management with Flask-Session
- JWT token validation and handshake processing
- Protected routes with authentication state
- User profile management

## Features

- **Clerk Authentication**: Seamless integration with Clerk for user authentication
- **Session Management**: Server-side session storage using Flask-Session
- **JWT Handshake**: Automatic processing of Clerk handshake tokens
- **Multiple Routes**: Home, plans, and profile pages with authentication context
- **Debug Logging**: Comprehensive logging for authentication events

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- A Clerk account with an application set up at [clerk.com](https://clerk.com)

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd flask-with-clerk
```

### 2. Configure Environment Variables

Create a `.env` file in the project root with your Clerk credentials:

```env
CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
FLASK_SESSION_SECRET=your-secret-key-here
APP_URL=http://localhost:5001
```

To obtain your Clerk keys:
1. Sign up at [clerk.com](https://clerk.com)
2. Create a new application
3. Copy your keys from the API Keys section in the Clerk Dashboard

### 3. Install Dependencies

Using uv:

```bash
uv sync
```

This will create a virtual environment and install all required dependencies specified in `pyproject.toml`.

## Running the Application

### Development Mode

```bash
uv run python main.py
```

The application will start on `http://localhost:5001` with debug mode enabled.

### Alternative: Using Flask CLI

```bash
uv run flask run --host=0.0.0.0 --port=5001
```

## Dependencies

- **flask** (>=3.1.2): Web framework
- **clerk-backend-api** (>=4.0.0): Clerk authentication SDK
- **flask-session** (>=0.8.0): Server-side session management
- **load-dotenv** (>=0.1.0): Environment variable loading
- **pyjwt** (>=2.10.1): JWT token handling

## How It Works

1. **Authentication Flow**: The application uses Clerk's authentication system to handle user sign-in/sign-up
2. **Handshake Processing**: Clerk handshake tokens from query parameters are decoded to extract authentication cookies
3. **Request Authentication**: Each request is authenticated using the Clerk Backend API before processing
4. **Session Storage**: Authentication state is stored in server-side sessions for quick access
5. **Template Rendering**: Templates receive authentication context to conditionally display content

## Available Routes

- `/` - Home page
- `/plans` - View subscription plans
- `/profile` - User profile (requires authentication)

## Development

### Viewing Logs

The application includes comprehensive logging. To see debug logs, check the console output when running the application.

### Modifying Templates

Templates use Jinja2 and include Clerk's client-side components. Edit files in the `templates/` directory to customize the UI.

## Troubleshooting

**Issue**: Application fails to start

- Verify all environment variables are set in `.env`
- Ensure Python 3.13+ is installed
- Run `uv sync` to reinstall dependencies

**Issue**: Authentication not working

- Check that your Clerk keys are correct
- Verify the APP_URL matches your application's URL
- Check the Clerk Dashboard for any configuration issues

**Issue**: Session errors

- Ensure the `flask_session/` directory exists and is writable
- Verify FLASK_SESSION_SECRET is set in `.env`

## Security Notes

- Never commit your `.env` file or expose your Clerk Secret Key
- The FLASK_SESSION_SECRET should be a strong, random value
- In production, use HTTPS and secure session cookies
- Configure proper CORS and authorized parties in Clerk Dashboard

## License

MIT

## Resources

- [Clerk Documentation](https://clerk.com/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [uv Documentation](https://github.com/astral-sh/uv)

