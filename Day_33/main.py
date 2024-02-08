import smtplib
import time

import requests
from datetime import *
import smtpd

MY_LAT=54.406867
MY_LNG=18.637555

MIN_LAT=MY_LAT-5
MAX_LAT=MY_LAT+5
MIN_LNG=MY_LNG-5
MAX_LNG=MIN_LNG+5

def is_night():

    paremetrs={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json", params=paremetrs)
    response.raise_for_status()

    data=response.json()
    print(data)
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])


    today=datetime.now()
    time_today=today.time().hour


    if time_today >sunset or time_today < sunrise:
        return True

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitute = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitute, latitude)

    if (longitute < MAX_LNG and longitute> MIN_LNG) and (latitude>MIN_LAT and latitude<MAX_LAT):
        return True

while True:
    time.sleep(60)
    if is_night() and is_overhead():
        mymail = "kyrielazone@gmail.com"
        password = "roer sreg gqot mwwp "

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mymail, password=password)
            connection.sendmail(from_addr=mymail, to_addrs="dominika.goik98@gmail.com", msg=f"Subject: Look up! \n\n Today ISS postion is {iss_position}, look for it in the sky!")

