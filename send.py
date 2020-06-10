# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC19cff6ac50db4a70262645b57ca3c9dc'
auth_token = '6a650a7b38b209b1d63f457eb697dddc'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="OMG I SAW YOU IN THIS VIDEO!!!",
                     from_='+12048139639',
                     to='+17789526396'
                 )

print(message.sid)
