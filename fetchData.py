def fetchCoordinates(cityName, countryCode):
    results = []
    try:
        response = session.get(f"http://api.openweathermap.org/geo/1.0/direct?q={cityName},{countryCode}&appid={api_key}")
        if response.status_code == 200:
            results = response.json()
        elif not results:
            print(f"No results found for {cityName}, {countryCode}. Check the spelling or the country code")
        latitude = results[0]["lat"]
        longitude = results[0]["lon"]
    
        return latitude, longitude
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}")

def fetchWeatherData(latitude, longitude):
    data = []
    try:
        response = session.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric")
        if response.status_code == 200:
            data = response.json()
        return data
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}")

