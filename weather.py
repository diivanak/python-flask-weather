from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="La Jolla"):

    lat, lon = 200, 200

    coord_request_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={os.getenv("API_KEY")}'

    json_data = requests.get(coord_request_url).json()

    if json_data:
        lat = json_data[0]["lat"]
        lon = json_data[0]["lon"]

    request_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv("API_KEY")}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or strings with extra spaces
    if not bool(city.strip()):
        city = "La Jolla"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)