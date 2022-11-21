# Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Example Input
# Angela, Ben, Jenny, Michael, Chloe

# Example Output
# Michael is going to buy the meal today!

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# using randint
random_index = random.randint(0, len(names)-1)
get_name = names[random_index]

# or using choise
# get_name = random.choice(names)

print(f'{get_name} is going to buy the meal today!')
