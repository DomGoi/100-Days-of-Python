import requests
import os
class NotificationManager:
    def __init__(self):
        self.account_sid="ACd9523a5cc270c13c323c29003afb676a"
        self.auth_token="574e7a21e1e3d7d969575b18822cf6f7"
        self.nr_twilio="+17163550664"
        self.my_nr="+48607723330"

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