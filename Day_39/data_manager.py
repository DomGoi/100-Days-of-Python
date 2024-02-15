import requests

class DataManager:
    def __init__(self):
        self.PROJECT_NAME = "prices"
        self.SHEET_NAME = "flightDeals"
        self.API_SHEETY_KEY = "657c33546299c858d6104f8fbeec3f34"
        self.get_endpoint = f"https://api.sheety.co/{self.API_SHEETY_KEY}/{self.SHEET_NAME}/{self.PROJECT_NAME}"
        self.post_endpoint = f"https://api.sheety.co/{self.API_SHEETY_KEY}/{self.SHEET_NAME}/{self.PROJECT_NAME}"
        self.put_endpoint = "https://api.sheety.co/db1d4275293be0fdbd88e663979b466f/flightDeals/prices/"

    # def get_the_location(self):
    #     self.resource_get = requests.get(url=self.get_endpoint)
    #     self.resource_get.raise_for_status()
    #
    #     data_get = self.resource_get.json()
    #     locations = []
    #     print(data_get)
    #     for cities in data_get['prices']:
    #         locations.append(cities["city"])
    #
    #     return locations

    # def get_the_prices(self):
    #     self.resource_get = requests.get(url=self.get_endpoint)
    #     self.resource_get.raise_for_status()
    #
    #     data_get = self.resource_get.json()
    #     prices = []
    #     for cities in data_get['prices']:
    #         prices.append(cities["lowestPrice"])
    #
    #     return prices
    #
    # def get_the_id(self):
    #     self.resource_get = requests.get(url=self.get_endpoint)
    #     self.resource_get.raise_for_status()
    #
    #     data_get = self.resource_get.json()
    #     ids = []
    #     for cities in data_get['prices']:
    #         ids.append(cities["id"])
    #
    #     return ids
    #
    # def get_the_code(self):
    #     self.resource_get = requests.get(url=self.get_endpoint)
    #     self.resource_get.raise_for_status()
    #
    #     data_get = self.resource_get.json()
    #     code = []
    #     for cities in data_get['prices']:
    #         code.append(cities["id"])
    #
    #     return code
    #
    # def price_locat(self):
    #     prices = self.get_the_prices()
    #     locations = self.get_the_location()
    #     ids = self.get_the_id()
    #     code = self.get_the_code()
    #     l_p = {}
    #     for pri, loc, ID, Code in zip(locations, prices, ids, code):
    #         l_p[pri, ID, Code] = {loc}
    #     return l_p

    def get_data_google(self):
        self.resource_get = requests.get(url=self.get_endpoint)
        self.resource_get.raise_for_status()
        self.data_google=self.resource_get.json()
        print(self.data_google["prices"])
        self.data_g=self.data_google["prices"]
        return self.data_g

    def write_google_code(self):
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        data = self.get_data_google()
        for n in range(0, len(self.data_google["prices"])):
            code = flight_search.get_code(self.data_google)  # Pass the entire data dictionary
            parameters_post_code = {
                "price": {
                    "code": code  # Code at the root level
                }
            }
            try:
                self.resource_put = requests.put(
                    url=f"https://api.sheety.co/db1d4275293be0fdbd88e663979b466f/flightDeals/prices/{self.data_google['prices'][n]['id']}",
                    json=parameters_post_code)
                self.resource_put.raise_for_status()

            except requests.exceptions.HTTPError as err:
                print(f"HTTP Error: {err}")
                print(f"Response content: {self.resource_put.content}")



    pass

data_man=DataManager()
data_man.write_google_code()