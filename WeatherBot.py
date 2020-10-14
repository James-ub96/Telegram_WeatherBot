import requests
import os
import pyowm
import pandas as pd
from datetime import datetime


def send_msg(text):
    token = "1296339800:AAFgR9pfNmFNIBVxTqdyFOUfGDeLwUSfqUY"
    chat_id = '1179304537'

    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    return results.json()


owm = pyowm.OWM('df4b51370d5a0384c5050e6c5caec480')
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=49.3200, lon=-123.0724)

RainyDay = []

for hour in a:
    dt_object = datetime.fromtimestamp(hour.ref_time)
    if dt_object.day != datetime.now().day:
        if hour.rain:
            dt_object = datetime.fromtimestamp(hour.ref_time)
            RainyDay.append(hour.rain)
df = []
df = pd.DataFrame.from_dict(RainyDay)
if not df.empty:
    if (df['1h'] > 0.3).any():
        send_msg('Today has over a Thirty Percent Chance of Rain, best to bring a coat!')
