from weather import get_current_weather
from server import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_weather():
    weather = get_current_weather("New York")
    assert weather is not None