# Write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
count = 0
for height in student_heights:
    sum += height
    count += 1

avg = round(sum/count)
print(avg)
