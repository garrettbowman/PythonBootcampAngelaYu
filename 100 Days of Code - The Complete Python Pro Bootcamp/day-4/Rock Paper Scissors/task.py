import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameimages = [rock, paper, scissors]
userchoice = input("rock paper or scissors: \n")
computerchoice = random.choice(["rock", "paper", "scissors"])
print(f"You chose: {userchoice}")
if userchoice == "rock":
    print(gameimages[0])
elif userchoice == "paper":
    print(gameimages[1])
elif userchoice == "scissors":
    print(gameimages[2])

print(f"Computer chose: {computerchoice}")  

if computerchoice == "rock":
    print(gameimages[0])
elif computerchoice == "paper":
    print(gameimages[1])
elif computerchoice == "scissors":
    print(gameimages[2])

if userchoice not in ["rock", "paper", "scissors"]:
    print("You lose, dummy")
else:
    if userchoice == computerchoice:
        print("Draw")
    elif userchoice == "rock" and computerchoice == "scissors":
        print("You win")
    elif userchoice == "paper" and computerchoice == "rock":
        print("You win")
    elif userchoice == "scissors" and computerchoice == "paper":
        print("You win")
    else:
        print("You lose")