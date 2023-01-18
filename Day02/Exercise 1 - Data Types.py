# Data types

# int
# str
# float
# bool

# Interchange between data types with casting
# Data types are flexible - dinamic typic (create a var and later change it's type)


# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Example Input
# 39
# Example Output
# 3 + 9 = 12
# 12

two_digit_number = input("Type a two digit number: ")
sum = int(two_digit_number[0])+int(two_digit_number[1])

split_nr = [int(d) for d in two_digit_number]
sum = 0
for nr in split_nr:
    sum += nr
print(sum)
