# Dictionary comprehension

# Creating a new dictionary from a previous list or dictionary

# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}

import pandas
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
student_scores = {name: random.randint(1, 101)for name in names}
print(student_scores)

passed_students = {student: score for (
    student, score) in student_scores.items() if score > 70}
print(passed_students)

# create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}

print(result)

# create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)

# Loop over Pandas DataFrame (though rows)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

df = pandas.DataFrame(student_dict)
print(df)

for (index, row) in df.iterrows():
    print(row.student)
