from turtle import Turtle, Screen
import random
import time

from main import snake_length


class Snake:

    def __init__(self):
        self.first_square = (0,0)
        self.snake_length =3
        self.squares = []
        for init in range(snake_length):

            square = Turtle(shape="square")
            square.penup()
            square.speed("slow")
            square.setx(0 + init * 20)
            square.penup()
            self.squares.append(square)

    def turn_right(self):
        self.squares[-1].setheading(0)

    def turn_left(self):
        self.squares[-1].setheading(180)

    def turn_up(self):
        self.squares[-1].setheading(90)

    def turn_down(self):
        self.squares[-1].setheading(270)

    def move(self):
        self.first_square = self.squares[-1].pos()
        first_square_head = self.squares[-1].heading()
        square = Turtle(shape="square")
        square.speed("slow")
        square.penup()
        square.setposition(self.first_square)
        square.setheading(first_square_head)
        square.forward(20)
        square.color("white")
        self.squares.append(square)

        self.squares[0].reset()

        del self.squares[0]

    def game_over(self):
        spot = self.squares[-1].pos()
        spots = []
        for _ in self.squares:
            spots.append(_.pos())
        if abs(spot[0]) > 280:
            return True
        elif abs(spot[1]) > 280:
            return True
        elif spot in spots:
            return True
        else:
            return False