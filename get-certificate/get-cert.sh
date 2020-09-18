#!/bin/sh
set +x
# Set parameters
hst=$1; shift
if [ $# -ge 1 ]; then
 prt=${1:-443}
 shift
else
 prt=443 
fi
# Extract Certificate Text
openssl  s_client -connect $hst:$prt $@ 2>/dev/null </dev/null  |\
 awk '/BEGIN CERTIFICATE/,/END CERTIFICATE/{print $0}'|\
 openssl x509 -noout -text 
