#!/bin/bash
# author: Ishraque Zahin

function usage {
cat <<EOM
Usage:
    $(basename $0) <insert_flag_here>
Description:
    This script generates a new message and public key to set up the challenge.
Note: 
    This uses a 192 bit modulus, hence plaintext can be upto 12 characters.
    This may not work with openssl versions newer than 1.0.1j as those specifically forbid
    creating keys with modulus smaller than 256/512 bit.
    Works with LibreSSL 2.8.3, which seems to be the default on MacOS.

EOM
exit 0
}

if [ -z $1 ]; then
    usage
fi
{ # try
    openssl genrsa 192 > orig.key
    openssl rsa -pubout -in orig.key > pub.key
    echo $1 | openssl rsautl -encrypt -inkey orig.key > message
} || { # catch
    rm orig.key
    usage
}
# finally
rm orig.key
echo "Success! Generated public key and message."
