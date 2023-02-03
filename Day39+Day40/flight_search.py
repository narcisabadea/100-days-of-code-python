import requests
from flight_data import FlightData
from configparser import ConfigParser
from pprint import pprint

flight_search_api = "https://api.tequila.kiwi.com"


def _get_api_key():
    config = ConfigParser()
    config.read("../secrets.ini")
    return config["flight"]["apikey"]


headers = {
    "apikey": _get_api_key()
}


class FlightSearch:
    def get_destination_code(self, city_name):
        # Use the Kiwi API to GET all the flight's code
        location_endpoint = f"{flight_search_api}/locations/query"

        query = {"term": city_name, "location_types": "city"}
        response = requests.get(
            url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{flight_search_api}/v2/search",
            headers=headers,
            params=query,
        )
        pprint(response.json()["data"][0])
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{flight_search_api}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
