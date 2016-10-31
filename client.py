#!/usr/bin/python
#
# Author: LukeBob
#
# Simple client to send the messages to the server.
#
# You can only send a message every 300 sec's, you can adjust this in the server.py, by changing the "Message delay" num lower or higher.

import socket


def Main():
    host = '127.0.0.1' # Server Host
    port = 50098       # Server Port
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    message = raw_input('Message => ')
    while message != 'q' and message != 'quit':
        s.send(message)
        message = raw_input('Message => ')
    s.close()

if __name__ == '__main__':
    Main()
