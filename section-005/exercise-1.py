#Write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0

for heigh in student_heights:
    total += heigh

print(round(total/len(student_heights)))