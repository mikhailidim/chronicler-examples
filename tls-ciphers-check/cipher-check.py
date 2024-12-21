#
import sys, csv
import socket, ssl
CIPHERS_FILE='ciphers.csv'

#Initialize default Security Context
context = ssl.create_default_context()

def loadCiphers(fName: str = CIPHERS_FILE) -> list:
    try:
        with open(CIPHERS_FILE) as csvfile:
            creader = csv.reader(csvfile)
            # Read cipher pairs into list of tuples. 
            # Skipping comments and empty lines. 
            cipher_names = [ tuple(row) for row in creader if len(row) > 0 and not row[0].startswith('#')]
            
    except Exception as e:
        print("WARNING: Use available list of ciphers. Failed to read cipher pairs. {cfile} due to {ex} "
            .format(cfile=CIPHERS_FILE,ex=e))    
        
        # Initialize with a client ciphers
        # Exclude TLSv1.3 protocol due to SSLSocket implementation specifics.  
        cipher_names = [('',item['name']) for item in context.get_ciphers() if 'TLSv1.3' not in item['protocol']]
        
    return cipher_names    

# Initialize remote address with the default value 
remote_addr = ('www.python.org',443)

#Process Parameters
def initParams(args: list): 
    if len(args) <2:
        raise RuntimeError("Not enough arguments.")
    addr = (args[1].split(':')[0],int(args[1].split(':')[1]))
    if len(args) >2: 
        ciphers = args[2].split(':')
    else:
        # Initialize the test list with default names
        # from client. Exclude TLSv1.3 suites  
        ciphers = [ item['name'] for item in context.get_ciphers() if 'TLSv1.3' not in item['protocol']]
    return addr,ciphers
    
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
def main() -> int:
    try:
        remote_addr,test_ciphers = initParams(sys.argv)
        print("Test secure connection for {host}:{port}".format(host=remote_addr[0],port=remote_addr[1]))
        cp_list = loadCiphers()
        for cp in test_ciphers:
            # Find cipher in a list
            ctpl = [item for item in cp_list if cp in item][0]
            # Set Context to OpenSSL cipher
            try:
                context.set_ciphers(ctpl[1])
                ssl_sock = context.wrap_socket(
                socket.socket(socket.AF_INET,socket.SOCK_STREAM),server_hostname=remote_addr[0])
                ssl_sock.connect(remote_addr)
                print("*\tSuccess with cipher {tc} ({oc})".format(tc=ctpl[0],oc=ctpl[1]))
            except ssl.SSLError:
                print("-\tFailed with cipher {tc} ({oc})".format(tc=ctpl[0],oc=ctpl[1])) 
            finally: 
                ssl_sock.close()    
    except RuntimeError:
        print("Run the script in format as follow:")
        print("$python {script} hostname:port [CIPHER[:NAMES[:LIST]]]".format(script=sys.argv[0]))
        return 1

if  __name__ == '__main__': 
    sys.exit(main())