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

**The Server** is part of the ***encrypted messaging tools***. **it uses a set password shared by client and server** and generates a **random iv** every new message. Also you can **define ip adresses allowed to connect** in **ip whitelist**. Its purpose is to **send encrypted messages** to the server who will **decrypt the message and text the phone number linked to the twillio API**.
