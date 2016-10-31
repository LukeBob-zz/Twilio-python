#!/usr/bin/python
#
# Author: LukeBob
#
# Simple client to send the messages to the server.
#
# You can only send a message every 300 sec's, you can adjust this in the server.py, by changing the "Message delay" num lower or higher.

import socket
from Crypto.Cipher import AES
import os
salt = '' # salt to be shared with server
key32 = "{: <32}".format(salt).encode("utf-8")
def main():
    host = '127.0.0.1' # Server Host
    port = 50097       # Server Port
    iv = os.urandom(16) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    message = raw_input('Message => ')
    obj = AES.new(key32, AES.MODE_CFB, iv)
    ciphertext = obj.encrypt(message)
    while message != 'q' and message != 'quit':
        iv = os.urandom(16) 
        s.send(ciphertext)
        message = raw_input('Message => ')
        obj = AES.new(key32, AES.MODE_CFB, iv)
        ciphertext = obj.encrypt(message)
    s.close()

if __name__ == '__main__':
    main()
