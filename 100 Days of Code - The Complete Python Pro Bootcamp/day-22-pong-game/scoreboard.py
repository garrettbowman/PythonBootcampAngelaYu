from turtle import Turtle, Screen
import random
import time



class Scoreboard(Turtle):
    """chose to keep separate turtles but could all be 1 I suppose"""
    def __init__(self):
        super().__init__()
        self.snake_length = 3
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.setposition(-50, 250)
        self.score.write(f"Score: {self.snake_length - 3}", font=('Arial', 18, 'normal'))


    def update_score(self,snake_length):

        self.score.reset()
        self.score.hideturtle()
        self.score.color("white")
        self.score.penup()

        self.score.setposition(-50, 250)
        self.score.write(f"Score: {snake_length - 3}", font=('Arial', 18, 'normal'))

    def game_over(self):
        # print("GG")
        self.its_over=Turtle()
        self.its_over.color("RED")
        self.its_over.penup()
        self.its_over.hideturtle()
        self.its_over.setposition(-80, 0)
        self.its_over.write(f"GAME OVER", font=('Arial', 18, 'normal'))