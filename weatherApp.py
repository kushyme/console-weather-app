#!/usr/bin/env python3
import requests
import os
from dotenv import load_dotenv
from terminaltables3 import AsciiTable
import sys
import * from fetchData



def getApiKey():
    load_dotenv()
    api_key = os.getenv('api_key')
    if not api_key:
        raise RuntimeError("No API key found. Set API key in the .env file.")
    return api_key

def asciiMenu(data, cityName):
    table_data = [
        [
            "Location", 
            "Current temperature",
            "Min. temperature", 
            "Max. temperature", 
            "Humidity", 
            "Description"
         ],
        [
            cityName, 
            data["main"]["temp"], 
            data["main"]["temp_min"], 
            data["main"]["temp_max"], 
            data["main"]["humidity"], 
            data["weather"][0]["description"]
        ]
    ]
    table = AsciiTable(table_data)
    print(table.table)

if __name__ == "__main__":
    if len(sys.argv) != 2: # might have to be a 3
        print("The right command is: weather <cityName> <countryCode>")
        sys.exit(1)

    cityName = sys.argv[1]
    countryCode = sys.argv[2]

    try:
        api_key = getApiKey()
        session = requests.session()
        latitude, logitude = fetchCoordinates(cityName, countryCode) # TODO: add runtime error
        data = fetchWeatherData(latitude, logitude) # TODO: add runtime error
    except RuntimeError as e:
        print(e)
        sys.exit(1)

    asciiMenu(data, cityName)
