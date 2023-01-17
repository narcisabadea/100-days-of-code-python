# API - application programming interface

# - is a set of commands, functions, protocols and objects that programmers can use to create software of interact with an external system
# - a barrier between my program and an external system
# - trying to use the rules that the API prescribed to make the request to the external system
# - if the request is accoring the the rules from the API then the external system will send back a response with the data that you want

# endpoint - the location that can be accessed to get the data

import requests

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=URL)
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
