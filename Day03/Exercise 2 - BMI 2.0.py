# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Example Input
# weight = 85
# height = 1.75
# Example Output
# 85 ÷ (1.75 x 1.75) = 27.755102040816325
# Your BMI is 28, you are slightly overweight.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/(height**2))
are = ''

if bmi < 18.5:
    are = "are underweight"
elif bmi > 18.5 and bmi < 25:
    are = "have a normal weight"
elif bmi > 25 and bmi < 30:
    are = "are slightly overweight"
elif bmi > 30 and bmi < 35:
    are = "are obese"
else:
    are = "are clinically obese"

print(f'Your BMI is {bmi}, you {are}.')