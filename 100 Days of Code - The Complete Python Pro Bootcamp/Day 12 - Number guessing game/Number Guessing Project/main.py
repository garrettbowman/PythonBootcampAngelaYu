import random

from art import logo

print(logo)

continueplaying = True
def calculate(guess, num):
    print(f"You are { guess } off")

while continueplaying:
    guessme = random.randint(1,100)
    mode = input("easy or hard mode?:")
    if mode == "hard":
        guesses = 5
    else:
        guesses = 10
    
    for i in range(0,guesses):
        if i == 0:
            userguess = input("what is your first guess?")
            calculate(userguess,guessme)
        elif i == 1:
            userguess = input("what is your 2nd guess?")
            calculate(userguess,guessme)
        elif i == 2:
            userguess = input("what is your 3rd guess?")
            calculate(userguess,guessme)
        else:
            userguess = input(f"what is your {i+1}th guess?")
            calculate(userguess,guessme)