import requests
import os
class NotificationManager:
    def __init__(self):
        self.account_sid="ACd9523a5cc270c13c323c29003afb676a"
        self.auth_token=os.environ["auth_token"]
        self.nr_twilio=os.environ["nr_Twilio"]
        self.my_nr=os.environ["my_nr"]

    def send_SMS(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body=message,
            from_=self.nr_twilio,
            to=self.my_nr
        )

        print(message.status)
    pass
