# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existing_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]


# TypeError
# text = "abc"
# print(text + 3)

# Catching an error
# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    # print(a_dict["non_existing_key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    # raise = raise our own exceptions
    raise TypeError("This is an error that I made up")
