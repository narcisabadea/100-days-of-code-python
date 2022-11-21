# Example Input 1
# column 2, row 3 would be entered as:

# 23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']

# Example Input 2
# column 3, row 1 would be entered as:

# 31
# Example Output 2
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

col = int(position[0])
row = int(position[1])

selected_row = map[row-1]
selected_row[col-1] = "X"

print(f"{row1}\n{row2}\n{row3}")