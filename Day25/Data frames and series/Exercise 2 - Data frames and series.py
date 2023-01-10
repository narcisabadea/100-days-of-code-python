
# Using Pandas - Python Data Analysis Library

# Pandas has 2 primary data structures: Series (1 dimensional) and DataFrames (2 dimensional)

import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
print(type(data))  # DataFrame - the whole table
print(type(data["temp"]))  # Series - one of the colums (a list

# Get Data in Column

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

avg_temp_pd = data["temp"].mean()
print(avg_temp_pd)

max_temp = data["temp"].max()
print(max_temp)

print(data.condition)

# Get Data in Row
row = data[data.day == "Monday"]
print(row)

row_high_temp = data[data.temp == data.temp.max()]
print(row_high_temp)

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp * 9/5)+32
print(f"{monday_temp} deg F")


# Create DataFrame

data_dict_students = {
    "students": ["Amy", "James", "Tim"],
    "scores": [76, 56, 65]
}

data_students = pandas.DataFrame(data_dict_students)
data.to_csv("new_data.csv")
print(data_students)
