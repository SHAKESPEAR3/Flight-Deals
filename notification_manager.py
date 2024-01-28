from twilio.rest import Client

account_sid = "ACaaa5fed9a247130bc352309b9997c947"
auth_token = "2dd0b2ac79d29168c65b8a233691ce2b"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_message(self):
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                             body=message,
                             from_='+15188643603',
                             to='+421944436207'
                         )

        print(message.status)