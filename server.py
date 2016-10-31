#!/usr/bin/python
#
# Author: Lukebob
#
# Requires the pip instilation of twilio, (pip install twilio)
#
# Requires "IPTABLES"
#
# Send a message to your Mobile using any Computer/Server running unix... Works but not yet finished.
#
# "MAKE SURE YOU WHITELIST YOUR IP IN THE TRUSTED LIST", if your using over wan use wan ip.

import socket
import time
from twilio.rest import TwilioRestClient
import subprocess
import sys, traceback
from Crypto.Cipher import AES
import os
accountSid = '' # Account sid
authToken = '' # Account auth token

salt = '' # salt to be shared with client
key32 = "{: <32}".format(salt).encode("utf-8")

def iptables(person):
    subprocess.call('/sbin/iptables -I INPUT -s '+person+' -j DROP',shell=True)

def Main():
    try:
        trusted = ['127.0.0.1'] # trusted ip list
        host = '127.0.0.1'  # server host
        port = 50097            # server port
        s = socket.socket()
        s.bind((host, port))
        s.listen(1)
        c, addr = s.accept()
        person = str(addr)
        person = person[1:-8]
        person = person.replace("'",'',2) # Person = client ip addr
        if person not in trusted:
            print '\nFailed Connection Occurance...\n'
            time.slpeep(1)
            iptables(person)      # Any ip not trusted gets banned
            time.sleep(1) 
            print 'Banned '+person+' with iptables!..'
                    
        while True:
            iv = os.urandom(16) 
            obj2 = AES.new(key32, AES.MODE_CFB, iv)           
            data = c.recv(1024)
            data = obj2.decrypt(data)         
            alldata = 'Data: '+data+' Recived From Host: '+person
            if not data:
                break
            client = TwilioRestClient(accountSid, authToken)
            client.messages.create( body=data, to=<Your Phone Number>, from_=<Twilio Phoone Number>) # Twilio, and own number here.
            subprocess.call('echo '+alldata+' >> TwilioData.txt', shell=True)
            time.sleep(300)  # Message delay
        c.close()
    except KeyboardInterrupt:
        print ("Exiting...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == '__main__':
    Main()
