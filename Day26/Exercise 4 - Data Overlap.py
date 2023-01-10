with open("file1.txt") as file1:
    data_1 = file1.readlines()


with open("file2.txt") as file2:
    data_2 = file2.readlines()

result = [int(number) for number in data_1 if number in data_2]

print(result)

