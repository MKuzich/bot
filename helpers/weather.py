"""Weather functions"""
import requests
from config import WEATHER_API, WEATHER_API_KEY
from helpers.location import get_location_info

def get_weather(lat, lon):
    url = f"{WEATHER_API}/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    request = requests.get(url, timeout=5)
    if request.status_code == 200:
        return request.json()
    return None

def get_weather_info():
    location = get_location_info()
    if location:
        return get_weather(location["lat"], location["lon"])
    return None
