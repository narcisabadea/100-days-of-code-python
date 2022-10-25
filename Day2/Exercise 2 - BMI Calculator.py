# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Example Input
# weight = 80
# height = 1.75
# Example Output
# 26

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight)/(float(height)**2)
print(int(bmi))