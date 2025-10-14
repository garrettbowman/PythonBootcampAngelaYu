from turtle import Turtle
import random
import time
from scoreboard import Scoreboard

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(0, random_y)
        self.penup()
        self.shape("circle")
        self.speed("slowest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.ball_spot = self.pos()


    def move(self):
        self.forward(1000)
    def change(self):
        self.penup()

        # random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(0, random_y)
        self.color("green")
        self.ball_spot = self.pos()