import random

from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def calculate(guess, num, i):
    '''Not the greatest organized calculation'''
    global correct, guesses, guessesleft, wrong
    if int(guess) == int(num):
        correct = True
        return
    
    guessesleft -= 1
    if guessesleft == 0:
        print("out of guesses")
        wrong = True
        return
    
    if int(num) - int(guess) > 0:
        print("Too low\nguess again")
    else:
        print("Too high\nguess again")
    print(f"You have { guesses - i -1 } guesses left")
    print(f"You are { int(num) - int(guess) } off\n")

def set_difficulty():
    mode = input("easy or hard mode?:")
    if mode == "hard":
        return HARD_TURNS
    else:
        return EASY_TURNS

# def correct():


continueplaying = True


while continueplaying:
    correct = False
    wrong = False
    print(logo)

    guessme = random.randint(1,100)
    guesses = set_difficulty()
    guessesleft = guesses

    for i in range(0,guesses+1):
        if correct == True:
            print("You got it")
            playagain = input("Play again? y or n: ")
            if playagain == "y":
                break
            else:
                continueplaying = False
                print("Goodbye")
                break
        elif wrong == True:
            print("You lose mate\n")
            playagain = input("Play again? y or n: ")
            if playagain == "y":
                break
            else:
                continueplaying = False
                print("Goodbye")
                break
        elif i == 0:
            userguess = input("what is your first guess? \n")
            calculate(userguess,guessme,i)
        elif i == 1:
            userguess = input("what is your 2nd guess? \n")
            calculate(userguess,guessme,i)
        elif i == 2:
            userguess = input("what is your 3rd guess? \n")
            calculate(userguess,guessme,i)
        else:
            userguess = input(f"what is your {i+1}th guess? \n")
            calculate(userguess,guessme,i)