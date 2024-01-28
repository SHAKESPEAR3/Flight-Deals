from twilio.rest import Client

account_sid = "your SID"
auth_token = "your TOKEN"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_message(self):
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                             body=message,
                             from_='+number',
                             to='+number'
                         )

        print(message.status)