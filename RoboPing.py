#!/usr/bin/python2.7
#
# Author: LukeBob
# text bot, Lets you know when your server goes down.
# Can be run on both windows and linux systems.
# requires twilio account and pip2.7 install twilio, twilio free account https://www.twilio.com
#
#
# Windows: PingBot.py, you will need the cmd prompt open at all times to keep the script running.
#
# Linux: ./PingBot.py, probably best off putting it inside a tmux session.


import os
import time
from twilio.rest import TwilioRestClient
import sys

ACCSID = 'AC'  # Account SID
AUTHTOK = ''   # Auth Token
name = os.name

if name == 'nt':
    windows = ('''        ###################
        #                 #
        # PingBot Windows #
        #                 #
        ###################''')
    print(windows)
else:
    Linux = ('''        ###################
        #                 #
        # PingBot Linux   #
        #                 #
        ###################''')
    print(Linux)


try:
    if name == 'nt':
        while 1:
            time.sleep(20)
            response = os.system('ping -n 1 <Server Name> 2>&1>nul')
            time.sleep(5)
            if response != 0:
                time.sleep(10)
                response = os.system('ping -n 1 <Server Name> 2>&1>nul')
                time.sleep(5)
                if response != 0:
                    client = TwilioRestClient(ACCSID, AUTHTOK)
                    client.messages.create( body="Server is Down", to="<Your Phone Num>", from_="<Twilio Phone Num>")
                    time.sleep(5)
                    sys.exit(0)

    else:
         while 1:
            time.sleep(20)
            response = os.system('ping -t 1 <Server Name> >>/dev/null')
            time.sleep(5)
            if response != 0:
                time.sleep(10)
                response = os.system('ping -t 1 <Server Name> >>/dev/null')
                time.sleep(5)
                if response != 0:
                    client = TwilioRestClient(ACCSID, AUTHTOK)
                    client.messages.create( body="Server is Down", to="<Your Phone Num>", from_="<Twilio Phone Num>")
                    time.sleep(5)
                    sys.exit(0)

except KeyboardInterrupt:
    print ("Exiting...")
except Exception:
    traceback.print_exc(file=sys.stdout)
sys.exit(0)
