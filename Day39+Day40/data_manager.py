import requests
from pprint import pprint

sheety_api = "https://api.sheety.co/d27e937eed74c1cbabaf96fd1251c54c/pythonDay39FlightDeals/prices"
sheety_api_users = "https://api.sheety.co/d27e937eed74c1cbabaf96fd1251c54c/pythonDay39FlightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out
        response = requests.get(url=sheety_api)
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_destination_codes(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_api}/{city['id']}",
                json=new_data
            )
            return response.text

    def get_customer_emails(self):
        customers_endpoint = sheety_api_users
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
