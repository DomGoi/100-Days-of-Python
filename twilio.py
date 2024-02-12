import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from datetime import *


#Aplhavantage api
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_STOCK_KEY=os.environ.get("api_stock_key")

#News Api
API_KEY_NEWS=os.environ.get("api_stock_news")


#Twilio api
account_sid="ACd9523a5cc270c13c323c29003afb676a"
auth_token=os.environ.get("auth_token")



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters={
    "symbol":STOCK,
    "apikey":API_STOCK_KEY
}

stock=requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY", params=parameters)
stock.raise_for_status()

#latest refreshed date
data_stock=stock.json()
print(data_stock)
last_date=max(data_stock["Time Series (Daily)"].keys())
data_stock_0=float(data_stock["Time Series (Daily)"][last_date]["4. close"])
print(data_stock_0)

#day before last registered date
last_date_dt=datetime.strptime(last_date,'%Y-%m-%d')
last_date_1_dt=last_date_dt-timedelta(days=1)
last_date_1=last_date_1_dt.strftime('%Y-%m-%d')
day_before_last_date=float(data_stock["Time Series (Daily)"][last_date_1]["4. close"])
print(day_before_last_date)

percentage_change=round(((data_stock_0 - day_before_last_date) / data_stock_0) * 100, 4)
print(percentage_change)

if percentage_change >= 1 or percentage_change<=-1:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    parameters_news = {
        "q": COMPANY_NAME,
        "from": last_date_dt,
        "to": last_date_dt,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": API_KEY_NEWS
    }

    news_api = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)
    news_api.raise_for_status()

    news_data = news_api.json()
    unique_des = []
    headlines_unique = []

    if "articles" in news_data:
        for article in news_data["articles"]:
            if "description" in article and article['description'] != "[Removed]":
                headlines = article["title"]
                print(headlines)
                short = article["description"]
                print(short)

                if short not in unique_des:
                    unique_des.append(short)
                    headlines_unique.append((headlines, short))
                    if len(headlines_unique) == 3:
                        break


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client=Client(account_sid, auth_token, http_client=proxy_client)

    body=f"TSLA: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change)}%\n"
    for headline, description in headlines_unique:
        body += f"\n{headline}\n{description}\n"

    message = client.messages.create(
        body=body,
        from_=os.environ.get("nr_Twilio"),
        to=os.environ.get("my_nr")
        )

    print(message.status)