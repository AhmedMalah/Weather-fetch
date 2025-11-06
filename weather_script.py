import requests
import os

# Get API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Cairo")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

if not API_KEY:
    print("Error: OPENWEATHER_API_KEY is missing!")
    exit(1)

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Weather in {CITY}: {temp}°C, {weather}")
else:
    print(f"Failed to fetch weather data: {response.status_code}")
