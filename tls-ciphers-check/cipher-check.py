#
import sys, csv
import socket, ssl
CIPHERS_FILE='ciphers.csv'
#Initialize default Security Context
context = ssl.create_default_context()

def loadCiphers(fName: str = CIPHERS_FILE) -> list:
    """
    The function `loadCiphers` reads cipher names from a CSV file or retrieves them from the default
    security context if the file is not found.
    
    :param fName: The `fName` parameter in the `loadCiphers` function is a string that represents the
    file name from which ciphers are loaded. By default, it is set to `CIPHERS_FILE`
    :type fName: str
    :return: A list of cipher names is being returned. If the 'ciphers.csv' file is successfully opened
    and read, function returns, the list of tuples with standard and OpenSSL cipher suite names. If file is missed or damaged 
    it returns an available list of names (OpenSSL only).
    """
    try:
        with open('ciphers.csv') as csvfile:
            creader = csv.reader(csvfile)
            cipher_names = [ tuple(row) for row in creader ]
    except:    
        cipher_names = [('',item['name']) for item in context.get_ciphers()]
    return cipher_names    

remote_addr = ('www.python.org',443)

def initParams(args: list): 
    if len(args) <2:
        raise RuntimeError("Not enough arguments.")
    addr = (args[1].split(':')[0],int(args[1].split(':')[1]))
    if len(args) >2: 
        ciphers = args[2].split(':')
    else: 
        ciphers = [ item['name'] for item in context.get_ciphers()]
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
            context.set_ciphers(ctpl[1])
            ssl_sock = context.wrap_socket(
                socket.socket(socket.AF_INET,socket.SOCK_STREAM),server_hostname=remote_addr[0])
            try:
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

