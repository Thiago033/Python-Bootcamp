#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

intHeight = float(height)
intWeight = float(weight)

bmi = intWeight / (intHeight * intHeight)

roundedBmi = round(bmi)

if roundedBmi < 18.5:
    print(f"Your BMI is {roundedBmi}, you are underweight.")
elif roundedBmi < 25:
    print(f"Your BMI is {roundedBmi}, you have a normal weight.")
elif roundedBmi < 30:
    print(f"Your BMI is {roundedBmi}, you are slightly overweight.")
elif roundedBmi < 35:
    print(f"Your BMI is {roundedBmi}, you are obese.")
else:
    print(f"Your BMI is {roundedBmi}, you are clinically obese.")