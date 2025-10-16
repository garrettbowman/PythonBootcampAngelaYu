import time
from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=700)
screen.bgcolor("black")
screen.title("My pong game")

r_paddle = Paddle("r")
l_paddle = Paddle("l")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.tracer(0)
screen.onkey(l_paddle.move_up, "q")
screen.onkey(l_paddle.move_down, "a")
screen.onkey(fun=r_paddle.move_up, key="e")
screen.onkey(r_paddle.move_down, "d")


centerline = Turtle(shape="turtle")
centerline.hideturtle()
centerline.penup()
centerline.goto(0,-300)
centerline.setheading(90)
centerline.color("white")
centerline.speed("fastest")

for x in range(31):
    centerline.pendown()
    centerline.forward(10)
    centerline.penup()
    centerline.forward(10)


over = False

while not over:
    ball.move()
    for segment in r_paddle.segments:
        if segment.distance(ball) <20:
            ball.hit_object("r")
            print("HIT")

    for segment in l_paddle.segments:
        if segment.distance(ball) <20:
            ball.hit_object("l")
            print("HIT")

    spot = ball.pos()
    if spot[1] > 290:
        ball.hit_object("t")
    elif spot[1] < -290:
        ball.hit_object("b")

    elif spot[0] > 360:
        scoreboard.left_score += 1
        scoreboard.update_score()
        ball.change("l")

    elif spot[0] < -360:
        scoreboard.right_score += 1
        scoreboard.update_score()
        ball.change("r")

    time.sleep(ball.ball_speed)
    screen.update()

screen.exitonclick()