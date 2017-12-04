[![Packagist](https://img.shields.io/badge/app-twillio-orange.svg)]()  [![Packagist](https://img.shields.io/badge/platform-win--64%20%7C%20linux--64%20%7C%20osx--64-lightgrey.svg)]()  [![Packagist](https://img.shields.io/badge/language-python3.5-brightgreen.svg)]()  
 

# Twilio-python

All scripts require pip instilation of twilio. (pip install twilio) 
Also, you must make a free account at **https://www.twilio.com**, after this you can aquire your **Account SID** and **Auth token.**

# Setup  

Extract the files to any folder, then give them all exe permissions like so.

* ``` git clone https://github.com/LukeBob/Twilio-python.git```
* ``` cd Twilio-python && chmod 755 *.py```
 
Then you can run the scripts...   ./myscript 

# RoboPing

**RoboPing** is a bot that pings your server every 20 seconds. if it gets no response it texts your mobile through the **Twillio API**.


# Server & client

Both client and server are part of the ***encrypted messaging tools***. **they use a set password shared by both client and server**. The client generates a **random iv** every new message. Also you can **define ip adresses allowed to connect** in **ip whitelist**. Its purpose is to **send encrypted messages** to the server who will **decrypt the message and text the phone number linked to the twillio API**.
