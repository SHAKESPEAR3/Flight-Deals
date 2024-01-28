import requests
from datetime import datetime, timedelta

API_KEY = "LOPEzqhiss2EZNklWzb3DyTjUrWsxT_M"

location_endpoint = "https://api.tequila.kiwi.com/locations/query"

fly_from = "VIE"
search_endpoint = "https://api.tequila.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_codes = []
        now = datetime.now()
        six_monthsfromnow = now + timedelta(days=6*30)
        self.date_from = now.strftime("%d/%m/%Y")
        self.date_to = six_monthsfromnow.strftime("%d/%m/%Y")

    def get_city_code(self, city):
        location_params = {
            "term": city,
            "location_types": "city",
        }

        response = requests.get(url=location_endpoint, headers={"apikey": API_KEY}, params=location_params)
        response.raise_for_status()
        data = response.json()
        self.city_codes.append(data["locations"][0]["code"])

    def get_flights(self, fly_from, fly_to, price_to):
        search_params = {
            "fly_from": f"city:{fly_from}",
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "price_to": price_to,
            "sort": "price",
            "limit": 1
        }

        response = requests.get(url=search_endpoint, headers={"apikey": API_KEY}, params=search_params)
        response.raise_for_status()
        data = response.json()
        return data


