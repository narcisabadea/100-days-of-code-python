# List comprehension

# Creating a new list from a previous list

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)


# with list comprehension it becomes

new_list = [n + 1 for n in numbers]

print(new_list)

# can work with strings as well
name = "Angela"
name_list = [letter for letter in name]

print(name_list)

# Python sequences: list, range, string, tuple

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# Conditional List Comprehension

# new list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]

names_list = [name for name in names if len(name) < 5]
uppercase_list = [name.upper() for name in names if len(name) > 4]
print(names_list)
print(uppercase_list)