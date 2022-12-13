# Write a program that converts scores to grades.

# This is the scoring criteria:

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    get_score = student_scores[student]

    if get_score > 90:
        student_grades[student] = "Outstanding"
    elif get_score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif get_score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
