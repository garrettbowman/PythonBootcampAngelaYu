from turtle import Turtle, Screen
import random
import time
import snake


class Scoreboard:

    def __init__(self):
        self.snake_length = 3
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.setposition(-50, 250)
        self.score.write(f"Score: {self.snake_length - 3}", font=('Arial', 18, 'normal'))


    def update_score(self):

        self.score.reset()
        self.score.hideturtle()
        self.score.color("white")
        self.score.penup()

        self.score.setposition(-50, 250)
        self.score.write(f"Score: {self.snake_length - 3}", font=('Arial', 18, 'normal'))