import os
from internetspeed import InternetSpeedTwitterBot

PROMISED_DOWN_MIN=225
PROMISED_UP_MIN=25
URL_1="https://twitter.com/i/flow/signup"

internet=InternetSpeedTwitterBot(PROMISED_DOWN_MIN,PROMISED_UP_MIN)
down,up, provider=internet.get_internet_speed()
if PROMISED_DOWN_MIN>int(down) or PROMISED_UP_MIN>int(up):
    internet.tweet_at_provider(down,up,provider)

