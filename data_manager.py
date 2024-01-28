import requests

SHEETY_GET_ENDPOINT = "https://api.sheety.co/02835cd482e16c380d46afc541fb9030/flightDeals/prices"
SHEETY_HEADER = {
    "Authorization": f"Bearer kjvnsjkcbkjbxjcU6"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        response = requests.get(url=SHEETY_GET_ENDPOINT, headers=SHEETY_HEADER)
        self.data = response.json()
        self.cities = []
        self.prices = []
        self.get_cities()
        self.get_price_to()



    def get_cities(self):
        for i in range(8):
            self.cities.append(self.data["prices"][i]["city"])

    def get_price_to(self):
        for i in range(8):
            self.prices.append(self.data["prices"][i]["lowestPrice"])

    def upload_city_code(self):
        SHEETY_PARAMS = {
            "price": {
                "iataCode": "Testing",
            }
        }
        for i in range(2, 11):
            SHEETY_PUT_ENDPOINT = f"https://api.sheety.co/02835cd482e16c380d46afc541fb9030/flightDeals/prices/{i}"
            response = requests.put(url=SHEETY_PUT_ENDPOINT, json=SHEETY_PARAMS, headers=SHEETY_HEADER)



dm = DataManager()
dm.upload_city_code()