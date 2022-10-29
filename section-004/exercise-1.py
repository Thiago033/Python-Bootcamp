#Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

randomNumber = random.randint(0,1)

if randomNumber == 1:
    print("Heads")
else:
    print("Tails")