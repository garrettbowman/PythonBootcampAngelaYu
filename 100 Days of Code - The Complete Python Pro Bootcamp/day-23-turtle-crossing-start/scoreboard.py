FONT = ("Courier", 24, "normal")
from turtle import *

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", font = FONT)

    def new_level(self):
        self.clear()
        self.score +=1
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(-80,0)
        self.pencolor("red")
        self.color("red")
        self.pendown()
        self.write(f"GAME OVER", font=FONT )