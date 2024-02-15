import requests
from datetime import datetime as dt, timedelta


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.API_KEY_KIWI="q35ORRv9RuDuoUJmw-cZ_zZbBJ5O11uA"
        self.get_endpoint="https://api.tequila.kiwi.com/locations/query"
        self.get_search="https://api.tequila.kiwi.com/v2/search"
        self.FROM="LON"
        self.from_time=dt.now().strftime("%d/%m/%Y")
        six_months=dt.now()+timedelta(days=30*6)
        self.six_months_ahead=six_months.strftime("%d/%m/%Y")

        self.headers={
            "apikey": self.API_KEY_KIWI
        }

    def get_code(self, data_g):
        for c in range(0, len(data_g['prices'])):
            self.parameters_get = {
                "term": data_g['prices'][c]['city']
            }
            self.resource_get = requests.get(url=self.get_endpoint, params=self.parameters_get, headers=self.headers)
            self.resource_get.raise_for_status()

            self.data_get = self.resource_get.json()
            code = self.data_get['locations'][0]["code"]
        return code

    def check_flights(self, data_g):

        for c in range(0,len(data_g['prices'])):
            query = {
                "fly_from":self.FROM,
                "fly_to": data_g['prices'][c]['code'],
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "EUR"
            }
            self.search_flight=requests.get(url=self.get_search, params=query, headers=self.headers)
            self.search_flight.raise_for_status()

            try:
                self.data_flight=self.search_flight.json()["data"][0]
            except IndexError:
                print(f"No flights found for {self.FROM}.")
                return None

            flight_data = FlightData(
                price=self.data_flight["price"],
                origin_city=self.data_flight["route"][0]["cityFrom"],
                origin_airport=self.data_flight["route"][0]["flyFrom"],
                destination_city=self.data_flight["route"][0]["cityTo"],
                destination_airport=self.data_flight["route"][0]["flyTo"],
                out_date=self.data_flight["route"][0]["local_departure"].split("T")[0],
                return_date=self.data_flight["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data



    pass






