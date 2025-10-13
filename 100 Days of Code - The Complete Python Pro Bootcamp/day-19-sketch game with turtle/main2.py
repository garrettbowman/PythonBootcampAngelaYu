from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput("Make your bet","Which turtle will win race? Color: ").lower()
print(user_bet)

colors = ["red","orange","yellow", "blue","green", "purple"]
names = ["tim","tom","tyrone","eric","bob","jake"]

turtles = []
# tim = Turtle(shape="turtlse")
# tim.penup()
# tim.goto(-220,100)
for color in range(0,len(colors)):
    name = str(names[color])

    name = Turtle(shape="turtle")

    name.color(colors[color])

    turtles.append(name)
    name.penup()
    name.goto(-220,100 - 30 *color)

screen.listen()
over = False

while not over:
    index = 0
    for aturtle in turtles:

        spot = aturtle.pos()
        if spot[0] >200:
            print(f"The {colors[index]} turtle wins!")
            if user_bet == colors[index]:
                print("You guessed correctly!")

            else:
                print("Better luck next time!")
            over = True
        else:
            aturtle.forward(random.randint(0,10))
            index +=1


screen.exitonclick()