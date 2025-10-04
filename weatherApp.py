#!/usr/bin/env python3
import requests
import os
from dotenv import load_dotenv
from terminaltables3 import AsciiTable
import sys
load_dotenv()
api_key = os.getenv('api_key')
if not api_key:
    print("no apikey found")
    sys.exit(1)


session = requests.session()
def fetchData(cityName, countryCode):
    results = []
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
    table_data = [
        ["Location", "Current temperature", "Min. temperature", "Max. temperature", "Humidity"],
        [cityName, data["main"]["temp"], data["main"]["temp_min"], data["main"]["temp_max"], data["main"]["humidity"]]
    ]
    table = AsciiTable(table_data)
    print(table.table)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("The right command is: weather <cityName> <countryCode>")
        sys.exit(1)
    cityName = sys.argv[1]
    countryCode = sys.argv[2]
    data, cityName = fetchData(cityName, countryCode)
    asciiMenu(data, cityName)



