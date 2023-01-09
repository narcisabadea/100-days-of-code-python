# Open the file using the build-in method open
# Read the file using the build-in method read which returns the content of the file
# Close the file using the build-in method close so the resources used to be released

file = open("file.txt")
contents = file.read()
print('1st way', contents)
file.close()

# Another way of doing it with closing the file by default

with open("file.txt") as new_file:
    new_contents = new_file.read()
    print('2nd way', new_contents)

# Writing to our file by changing the mode from read-only to editable
# Mode w overiwrites the file, mode a appends to the existing text

with open("file.txt", mode='a') as write_file:
    write_file.write("\nYey!")

# If the file we try to open does not exist it will be created for us

with open("new_file.txt", mode='w') as write_file:
    write_file.write("New file created!")
