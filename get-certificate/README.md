# Read Server Certificate

Shell script to read certificate from host [get-cert.sh](./get-cert.sh)

Ways to call:
```bash
 $get-cert.sh <hostname> [port] [ s_client arguments]
 ```
 
Script accept parameters: 
 - __hostname__             Host or IP addres to where you want to read certificate 
 - __port__                 Port to connect to host. Options, Default value is 443.
 - __s_client arguments__  any arguemts that openssl s_client will accept, for example _-servername abc.de.com_.
   

