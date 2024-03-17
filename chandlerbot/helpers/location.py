"""Helpers function to get user location"""
import requests
from chandlerbot.config import IP_API

def get_location_info():
    request = requests.get(f"{IP_API}/json/?fields=61439", timeout=5)
    if request.status_code == 200:
        return request.json()
    return None
