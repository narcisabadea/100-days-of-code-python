import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

URL = "https://opentdb.com/api.php"
response = requests.get(url=URL, params=parameters)
data = response.json()
question_data = data["results"]
