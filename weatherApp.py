import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')
session = requests.session()

def fetchData():
    results = []
    cityName = input("Please enter the city name: ")
    countryCode = input("Please enter the country code (example: de, au, ja): ")
    try:
        response = session.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cityName},{countryCode}&appid={api_key}")
        if response.status_code == 200:
            results = response.json()
    except requests.RequestException as e:
        print(e)

    latValue = results[0]["lat"]
    lonValue = results[0]["lon"]

    data = []
    try:
        response2 = session.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latValue}&lon={lonValue}&appid={api_key}&units=metric")
        if response2.status_code == 200:
            data = response2.json()
    except requests.RequestException as e:
        print(e)

    return data,cityName

def asciiMenu(data, cityName):
    print(f"""
+----------+---------------------+------------------+------------------+----------+
| Location | Current temperature | Min. temperature | Max. temperature | Humidity |
+----------+---------------------+------------------+------------------+----------+
| {cityName:<14}   |               {data["main"]["temp"]:>19} |            {data["main"]["temp_min"]:>16} |            {data["main"]["temp_max"]:>16} |       {data["main"]["humidity"]:>8} |
+----------+---------------------+------------------+------------------+----------+

""")

while True:
    data, cityName = fetchData()
    asciiMenu(data, cityName)