# Write a program that calculates the sum of all the even numbers from 1 to 100.

sum = 0
for n in range(2,101, 2):
    sum += n

print(sum)