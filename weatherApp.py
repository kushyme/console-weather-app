import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')
session = requests.session()

cityName = input("Please enter the city name: ")
countryCode = input("Please enter the country code (example: de, au, ja): ")

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
    response2 = session.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latValue}&lon={lonValue}&appid={api_key}")
    if response2.status_code == 200:
        data = response2.json()
except requests.RequestException as e:
    print(e)

print(data)
# tempKelvin = data[2]["temp"] not working yet
#print(tempKelvin)