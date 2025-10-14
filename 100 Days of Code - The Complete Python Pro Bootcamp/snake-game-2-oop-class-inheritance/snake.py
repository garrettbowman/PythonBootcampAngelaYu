from turtle import Turtle, Screen
import random
import time

STARTING_POSITIONS = [(40,0),(20,0),(0,0)]
MOVEMENT_SPEED = 20

class Snake:

    def __init__(self):

        self.snake_length =3
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_spot = self.segments[0].pos()

    def create_snake(self):
        for _ in range(0,len(STARTING_POSITIONS)):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.speed("fastest")
            segment.goto(STARTING_POSITIONS[_][0],STARTING_POSITIONS[_][1])
            segment.penup()
            self.segments.append(segment)

    def turn_right(self):
        self.segments[0].setheading(0)

    def turn_left(self):
        self.segments[0].setheading(180)

    def turn_up(self):
        self.segments[0].setheading(90)

    def turn_down(self):
        self.segments[0].setheading(270)

    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            self.segments[segment].goto(self.segments[segment-1].pos())
        self.head.forward(MOVEMENT_SPEED)
        self.head_spot = self.segments[0].pos()

    def extend(self):
        self.snake_length +=1
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.speed("fastest")
        # last = self.segments[-1].pos()
        segment.goto(self.segments[-1].pos())
        segment.penup()
        self.segments.append(segment)

    def game_over(self):
        spot = self.segments[0].pos()
        spots = []
        # for _ in range(1,len(self.segments)):
        #     spots.append(self.segments[_].pos())
        #     if self.segments[_].distance(self.segments[0]) < 11:
        #         return True
        for _ in self.segments[1:]:
            if _.distance(self.segments[0]) < 11:
                return True
        if abs(spot[0]) > 280:
            return True
        elif abs(spot[1]) > 280:
            return True
        # elif self.segments[0].distance(spot)< 5:
        #     return True
        else:
            return False