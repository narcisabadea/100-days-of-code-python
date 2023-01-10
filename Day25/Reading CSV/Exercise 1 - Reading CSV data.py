with open("weather_data.csv") as file:
    data = file.readlines()
    print("Regular readlines", data)

# Using build in csv reader module

import csv

with open("weather_data.csv") as file:
    temperatures = []
    data = csv.reader(file)
    for index, row in enumerate(data):
        if index > 0:
            temperatures.append(int(row[1]))
    print("Using csv reader", temperatures)


# Using Pandas - Python Data Analysis Library

import pandas

data = pandas.read_csv("weather_data.csv")
print("Using pandas", data)
print(data["temp"])
