import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    if not API_KEY:
        print("ERROR: WEATHER_API_KEY not found in .env")
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        print("STATUS CODE:", response.status_code)
        print("API RESPONSE:", response.text)

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException as error:
        print("REQUEST ERROR:", error)
        return None