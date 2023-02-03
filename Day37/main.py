# Habit Tracking Project: API Post Requests & Headers

# API Post Requests
# - get: request an external service for a particular piece of data and they give it to us in a response
# - post: request where we give the external service a piece of data and we are interensted from the response if it was sucessful or not
# - put: request where we update a piece of date in the external service
# - delete: request where we delete a pierce of data in the external service

import requests
from datetime import datetime

USERNAME = "narcisabadea"
TOKEN = "7qvt6T2738qjwdwbdejfkew!"
GRAPH_ID = "test-graph"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create user account with POST request
# https://pixe.la/@narcisabadea

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph with POST request
# https://pixe.la/v1/users/narcisabadea/graphs/test-graph.html

response = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Create today's pixel with POST request

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data, headers=headers)

print(response.text)


# Update today's pixel with PUT request
new_pixel_data = {
    "quantity": "4.5"
}
# response = requests.put(url=update_endpoint,
#                         json=new_pixel_data, headers=headers)
# print(response.text)


# Delete today's pixel with DELETE request
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
