import requests
from config import GOOGLE_API_KEY

def get_traffic_data(origin, destination):
    url = (
        f"https://maps.googleapis.com/maps/api/directions/json"
        f"?origin={origin}&destination={destination}"
        f"&departure_time=now&key={GOOGLE_API_KEY}"
    )
    response = requests.get(url)
    return response.json()
