# file = open('section-024\my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

with open('section-024/example-01/my_file.txt') as file:
    contents = file.read()
    print(contents)
    
with open('section-024/example-01/my_file.txt', 'w') as file:
    file.write("New Text")
    
with open('section-024/example-01/my_file.txt', 'a') as file:
    file.write(" Append new text")
