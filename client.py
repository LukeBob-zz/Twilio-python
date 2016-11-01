#!/usr/bin/python
#
# Author: LukeBob
#
# Simple client to send the messages to the server.
#
# You can only send a message every 300 sec's, you can adjust this in the server.py, by changing the "Message delay" num lower or higher.
import hashlib
import socket
from Crypto.Cipher import AES
import os
import sys

key32 = hashlib.sha256("test password").digest()
iv = hashlib.sha256("test password").digest()[:16]

def main():
    host = '127.0.0.1' # Server Host
    port = 50098       # Server Port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    message = raw_input('Message => ')
    obj = AES.new(key32, AES.MODE_CFB, iv)
    ciphertext = obj.encrypt(message)
    while message != 'q' and message != 'quit':
        obj = AES.new(key32, AES.MODE_CFB, iv) 
        s.send(ciphertext)
        message = raw_input('Message => ')
        obj = AES.new(key32, AES.MODE_CFB, iv)
        ciphertext = obj.encrypt(message)
    s.close()

if __name__ == '__main__':
    main()
