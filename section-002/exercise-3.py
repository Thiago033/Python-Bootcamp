#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age?")

# days
x = (90 - int(age)) * 365
# weeks
y = (90 - int(age)) * 52
# months
z = (90 - int(age)) * 12

print(f'You have {x} days, {y} weeks, and {z} months left.')