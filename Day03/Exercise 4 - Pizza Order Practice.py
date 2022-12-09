# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

sum = 0

if size == 'S':
    sum += 15
elif size == 'M':
    sum +=20
else: 
    sum +=25

if add_pepperoni == 'Y':
    if size == 'M' or size == 'L':
        sum +=3

if extra_cheese == 'Y':
    sum += 1

print(f'Your final bill is: ${sum}.')