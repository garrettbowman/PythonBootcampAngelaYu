from turtle import Turtle, Screen
import random
import time



class Scoreboard(Turtle):
    """chose to keep separate turtles but could all be 1 I suppose"""
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.setposition(-65, 250)
        self.score.write(f"{self.left_score}       {self.right_score}", font=('Trebuchet MS', 30, 'bold'))


    def update_score(self):

        self.score.reset()
        self.score.hideturtle()
        self.score.color("white")
        self.score.penup()

        self.score.setposition(-65, 250)
        self.score.write(f"{self.left_score}       {self.right_score}", font=('Trebuchet MS', 30, 'bold'))

    # def game_over(self):
    #     # print("GG")
    #     self.its_over=Turtle()
    #     self.its_over.color("RED")
    #     self.its_over.penup()
    #     self.its_over.hideturtle()
    #     self.its_over.setposition(-80, 0)
    #     self.its_over.write(f"GAME OVER", font=('Arial', 18, 'normal'))