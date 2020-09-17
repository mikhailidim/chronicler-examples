#!/bin/sh
set +x
# Set parameters
hst=$1
prt=${2:-443}

# Extract Certificate Text

openssl  s_client -connect $hst:$prt $3 </dev/null 2>/dev/null |awk '/BEGIN CERTIFICATE/,/END CERTIFICATE/{print $0}'| openssl x509 -noout -text


