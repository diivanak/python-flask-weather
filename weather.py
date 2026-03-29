from dotenv import load_dotenv
from pprint import pprint
import requests
import os

DEFAULT_CITY = "La Jolla"
DEFAULT_LAT = 32.8328
DEFAULT_LON = -117.2713

load_dotenv()

def get_current_weather(city="La Jolla"):

    lat, lon = 200, 200 # Default values to trigger API error if coordinates are invalid

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not set in environment")
    
    if not city.strip():
        lat, lon = DEFAULT_LAT, DEFAULT_LON

    coord_request_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    coord_data = requests.get(coord_request_url).json()

    json_data = coord_data

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