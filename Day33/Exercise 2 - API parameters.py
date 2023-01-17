import requests
import datetime as dt

datetime = dt.datetime
URL = "https://api.sunrise-sunset.org/json"

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}
response = requests.get(url=URL, params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now)
