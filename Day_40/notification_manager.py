import os

from twilio.rest import Client
import smtplib

TWILIO_SID = os.environ["Twilio_SID"]
TWILIO_AUTH_TOKEN = os.environ["Token_twilio"]
TWILIO_VIRTUAL_NUMBER = os.environ["TwilioNR"]
TWILIO_VERIFIED_NUMBER =os.environ["MYNR"]

MY_EMAIL=os.environ["My_mail"]
MY_PASSWORD=os.environ["password"]
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

     def send_emails(self, emails, message):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                for email in emails:
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                    )