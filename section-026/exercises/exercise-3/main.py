# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

with open("section-026/exercise-3/file-1.txt") as file_1:
    list_1 = file_1.readlines()
    
with open("section-026/exercise-3/file-2.txt") as file_2:
    list_2 = file_2.readlines()

result = [int(number) for number in list_1 if (number in list_2)]

print(result)
