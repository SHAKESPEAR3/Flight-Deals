from data_manager import DataManager
from flight_search import FlightSearch

fly_from = "VIE"
flights = []

data_manager = DataManager()
flight_search = FlightSearch()


for city in data_manager.cities:
    city_code = flight_search.get_city_code(city)
    # data_manager.upload_city_code(city_code)


for n in range(len(flight_search.city_codes)):
    flight_data = flight_search.get_flights(fly_from=fly_from,
                              fly_to=flight_search.city_codes[n],
                              price_to=data_manager.prices[n]
                              )
    flights.append(flight_data["data"])

for flight in flights:
    if flight:
        print(f"from: {flight[0]['cityFrom']}")
        print(f"to: {flight[0]['cityTo']}")
        print(f"price: {flight[0]['price']}")
        print({flight[0]['local_departure'].split('T')[0]})
        print("\n")

