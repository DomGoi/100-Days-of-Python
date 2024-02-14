import os

import requests
from datetime import datetime

GENDER ="female"
WEIGHT_KG = os.environ["Weight"]
HEIGHT_CM = os.environ["Height"]
AGE ="26"

#Nutritionix part
nutri_ID=os.environ["NUTRI_ID"]
nutri_api_key=os.environ["API_KEY_NUTRI"]
headers={
    "x-app-id":nutri_ID,
    "x-app-key":nutri_api_key
}

excercise_input=input("What exercise did you do?").strip().lower()
parameters={
    "query": excercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
endpoint_nutri="https://trackapi.nutritionix.com/v2/natural/exercise"
resources=requests.post(url=endpoint_nutri, headers=headers, json=parameters)
resources.raise_for_status()

data=resources.json()


#Getting date
today=datetime.now().strftime("%d/%m/%Y")
today_time=datetime.now().strftime("%H:%M:%S")


# Sheety
sheet_name=os.environ["Sheet"]
project_name=os.environ["Project"]
api_key_sheety=os.environ["API_SHEETY"]
autho_Token=os.environ["Auth_token"]
headers_sheety={
"Authorization": autho_Token
}
endpoint_post=f"https://api.sheety.co/{api_key_sheety}/{project_name}/{sheet_name}"

for excercise in data["exercises"]:
    duration_formatted = f"{excercise['duration_min']:02d} min"
    parameters={
        "workout":{
        "date": today,
        "time":today_time,
        "exercise":excercise["name"].title(),
        "duration":duration_formatted,
        "calories":excercise["nf_calories"]
}
    }
    posting=requests.post(url=endpoint_post, json=parameters, headers=headers_sheety)

print(posting.status_code)