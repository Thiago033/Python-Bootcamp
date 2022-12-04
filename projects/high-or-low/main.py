import os
import random
from art import logo, vs
from gamedata import data

clear = lambda: os.system('cls')


def getRandomAccount():
    return random.choice(data)

def formatData(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    
    return f"{name}, a {description}, from {country}"


def checkAnswer(guess, A, B):
  if A > B:
    return guess == "a"
  else:
    return guess == "b"

def game():
    print(logo)
    
    score = 0
    continueGame = True
    
    accountB = getRandomAccount()
    
    while continueGame:
        
        accountA = accountB
        accountB = getRandomAccount()
        
        print(f"Compare A: {formatData(accountA)}.")
        print(vs)
        print(f"Against B: {formatData(accountB)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        folowsA = accountA["follower_count"]
        folowsB = accountB["follower_count"]
        
        isCorrect = checkAnswer(guess, folowsA, folowsB)
        
        clear()
        print(logo)
        if isCorrect:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continueGame = False
            print(f"Sorry, that's wrong. Final score: {score}")
        
game()