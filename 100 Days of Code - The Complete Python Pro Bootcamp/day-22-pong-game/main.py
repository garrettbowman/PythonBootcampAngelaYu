import time
from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(height=600, width=700)
screen.bgcolor("black")
screen.title("My pong game")

r_paddle = Paddle("r")
l_paddle = Paddle("l")
ball = Ball()

screen.listen()
# screen.tracer(0)
screen.onkey(l_paddle.move_up, "q")
screen.onkey(l_paddle.move_down, "a")
screen.onkey(fun=r_paddle.move_up, key="e")
screen.onkey(r_paddle.move_down, "d")

over = False

while not over:
    ball.move()

    # time.sleep(0.1)
    # screen.update()

screen.exitonclick()