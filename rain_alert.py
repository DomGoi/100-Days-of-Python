import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



account_sid="ACd9523a5cc270c13c323c29003afb676a"
auth_token=os.environ.get("auth_tokeN")

API_key=os.environ.get("OMW_key")
MY_LAT=54.406867
MY_LNG=18.637555

parameters={
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid": API_key,
    "units":"metric",
    "cnt":4
}

resource=requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
resource.raise_for_status()


data=resource.json()


#running
is_raining = False
thunderstorm = False
drizzle = False
snowing = False
for n in range(0,1):
    id = data["list"][n]["weather"][0]["id"]
    if id >= 200 and id < 300:
        thunderstorm = True
    elif id >= 300 and id < 400:
        drizzle = True
    elif id >= 500 and id < 600:
        is_raining = True
    elif id >= 600 and id < 700:
        snowing = True



if is_raining:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client=Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It will rain",
        from_=os.environ.get("Twilio_nr"),
        to=os.environ.get("my_nr")
    )
    print(message.status)

if thunderstorm:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client=Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Thunderstorm is coming",
        from_=os.environ.get("Twilio_nr"),
        to=os.environ.get("my_nr")
    )
    print(message.status)

if drizzle:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client=Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will drizzle",
        from_=os.environ.get("Twilio_nr"),
        to=os.environ.get("my_nr")
    )
    print(message.status)

if snowing:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client=Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will snow",
        from_=os.environ.get("Twilio_nr"),
        to=os.environ.get("my_nr")
    )
    print(message.status)