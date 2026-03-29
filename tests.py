from weather import get_current_weather, DEFAULT_CITY
from server import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_weather():
    weather = get_current_weather("La Jolla")
    assert weather is not None
    assert weather["name"].lower() == "la jolla"

def test_weather_not_found():
    weather = get_current_weather("ThisCityDoesNotExist")
    assert weather['cod'] == '400'

def test_weather_empty_city():
    weather = get_current_weather("")
    assert weather is not None
    assert weather["name"].lower() == DEFAULT_CITY.lower()
    assert "weather" in weather