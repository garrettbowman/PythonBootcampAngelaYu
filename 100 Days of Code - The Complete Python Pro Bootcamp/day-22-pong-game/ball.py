from turtle import Turtle
import random
import time

BALL_SPEED = 10

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
        self.setheading(random.randint(-30,30))
        self.ball_spot = self.pos()
        self.ball_speed = 0.1


    def move(self):
        self.forward(BALL_SPEED)
        self.ball_spot = self.pos()
    def change(self, w):
        self.penup()
        self.ball_speed =0.1
        # random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(0, random_y)
        if w == "l":
            self.setheading(random.randint(-50,50))
        elif w == "r":
            self.setheading(random.randint(130,220))
        self.color("white")
        self.ball_spot = self.pos()

    def hit_object(self,obj):

        if obj == "r":
            self.ball_speed *= 0.9
            if self.heading() <90:
                self.setheading(180-self.heading())
            else:
                self.setheading(360-self.heading()+180)

        if obj == "l":
            self.ball_speed *= 0.9
            if self.heading() <180:
                self.setheading(180-self.heading())
            else:
                self.setheading(360-self.heading()+180)


        if obj == "t":
            if self.heading() <90:
                self.setheading(360-self.heading())

            else:
                self.setheading(180-self.heading()+180)

        if obj == "b":
            if self.heading() <270:
                self.setheading(180 -self.heading()-180 )

            else:
                self.setheading(360-self.heading())