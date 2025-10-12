# from turtle import Turtle,Screen
from turtle import *
import random
import heroes


def random_color():
    return tuple((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

print(heroes.gen())
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(0)
screen = Screen()
screen.colormode(255)


# for _ in range(8):
#     # timmy_the_turtle.forward(10)
#     # timmy_the_turtle.pencolor("#FFFFFF")
#     # timmy_the_turtle.forward(10)
#     # timmy_the_turtle.pencolor("#000000")
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# for shape in range(3,11):
#
#     timmy_the_turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     for side in range(shape):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/shape)

while True:
    for x in range(0,360,10):
        timmy_the_turtle.pencolor(random_color())
    # # timmy_the_turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # # timmy_the_turtle.forward(100)
         # timmy_the_turtle.setheading(random.choice([0,90,180,270]))
        timmy_the_turtle.setheading(x)
        timmy_the_turtle.circle(100)
screen = Screen()
screen.colormode(255)
screen.exitonclick()

