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

userchoice = input("rock paper or scissors: ")
computerchoice = random.choice(["rock", "paper", "scissors"])
print("You chose: " + userchoice)
print("Computer chose: " + computerchoice)

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