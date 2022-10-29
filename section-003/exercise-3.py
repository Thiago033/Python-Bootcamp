#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

year = int(input("Which year do you want to check? "))

intYear = int(year)
if (intYear % 4) == 0:
    if (intYear % 100) == 0:
        if (intYear % 400) == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
