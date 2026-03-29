from weather import get_current_weather
from server import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_weather():
    weather = get_current_weather("New York")
    assert weather is not None

def test_weather_not_found():
    weather = get_current_weather("ThisCityDoesNotExist")
    assert weather['cod'] == '404'

def test_weather_empty_city():
    weather = get_current_weather("")
    assert weather is not None