# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

age = input("What is your current age?")

years_left = 90 - int(age)
calculated_days = years_left * 365
calculated_weeks = years_left * 52
calculated_months = years_left * 12

print(f'You have {calculated_days} days, {calculated_weeks} weeks, and {calculated_months} months left.')
