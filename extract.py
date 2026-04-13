##

import requests

def extract_weather():
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "start_date": "2026-04-10",
        "end_date": "2026-04-11",
        "hourly": ["temperature_2m", "rain", "wind_speed_10m", "wind_direction_10m", "weather_code"],
    }
    response = requests.get(url, params=params)
    data = response.json()
    return(data)

print(extract_weather())
