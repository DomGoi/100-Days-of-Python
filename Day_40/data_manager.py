import os
from pprint import pprint
import requests
SHEET_NAME = "prices"
PROJECT_NAME = os.environ["project"]
API_SHEETY_KEY = os.environ["KEY_API_SHEETY"]
SHEETY_PRICES_ENDPOINT =f"https://api.sheety.co/{API_SHEETY_KEY}/{PROJECT_NAME}/{SHEET_NAME}"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheet = "users"


        self.post_sheety = f"https://api.sheety.co/{API_SHEETY_KEY}/{SHEET_NAME}/{self.sheet}"

        self.Berer = os.environ["beacon_sheety"]

        self.headers = {
            "Authorization": self.Berer
        }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)


    def post_user_sheety(f_name, l_name, mail_1):
        parameters = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": mail_1
            }
        }
        resource_post = requests.post(url=f_name.post_sheety, json=parameters)
        resource_post.raise_for_status()
        print("Success, your mail will be added to the database.")

    def get_mail(self):
        customer_endpoint=f"https://api.sheety.co/ {self.user_key}/ {self.project}/ {self.sheet}"
        response=requests.get(url=customer_endpoint)
        data=response.json()
        self.customer_data=data['users']
        return self.customer_data
