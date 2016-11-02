#!/usr/bin/python2.7
#
# Author: LukeBob
#
# Creates a random iv and sends it before the cyphertext the server then
# gets the iv and decrypts the ciphertext using the shared key and cypher.


import hashlib
import socket
from Crypto.Cipher import AES
import os
import sys
import time
from Crypto import Random
import random

key32 = hashlib.sha256("test password").digest()[:256] # Super secret password shared with server.

def main():
    try:
        iv = Random.get_random_bytes(16)
        host = '127.0.0.1' # Server Host
        port = 50098       # Server Port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        message = raw_input('Message => ')
        obj = AES.new(key32, AES.MODE_CFB, iv)
        ciphertext = obj.encrypt(message)
  
        while message != 'q' and message != 'quit':
            s.send(iv)
            time.sleep(5)
            s.send(ciphertext)
            iv = Random.get_random_bytes(16)
            message = raw_input('Message => ')
            obj = AES.new(key32, AES.MODE_CFB, iv)
            ciphertext = obj.encrypt(message)
            time.sleep(2)
        s.close()

   
    except KeyboardInterrupt:
        print ("Exiting...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == '__main__':
    main()
