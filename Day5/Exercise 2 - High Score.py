# Write a program that calculates the highest score from a List of scores.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high = 0

for score in student_scores:
    if score > high:
        high = score

print(f"The highest score in the class is: {high}")
