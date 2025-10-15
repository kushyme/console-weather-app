def fetchLongitudeAndLatitude(cityName, countryCode):
    results = []
    try:
        response = session.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cityName},{countryCode}&appid={api_key}")
        if response.status_code == 200:
            results = response.json()
        elif not results:
            print(f"No results found for {cityName}, {countryCode}. Check the spelling or the country code")
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)

    latValue = results[0]["lat"]
    lonValue = results[0]["lon"]
    
    return latValue, lonValue


def fetchWeatherData(latVaule, lonValue):
    data = []
    try:
        response = session.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latValue}&lon={lonValue}&appid={api_key}&units=metric")
        if response.status_code == 200:
            data = response.json()
    except requests.RequestException as e:
        print(f"Network error: {e}")

    return data


