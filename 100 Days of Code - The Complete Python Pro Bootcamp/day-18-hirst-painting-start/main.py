# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
#
# print(rgb_colors)
#
# print(colors)
import random
import turtle

real_colors = [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

painter = turtle.Turtle()
turtle.colormode(255)
painter.penup()
painter.hideturtle()
screen = turtle.Screen()
painter.speed("fastest")

for row in range(-250,250,50):
    for column in range(-250,250,50):

        painter.setx(column)
        painter.sety(row)
        # painter.pencolor(random.choice(real_colors))
        # painter.fillcolor((random.choice(real_colors)))
        # turtle.begin_fill()
        painter.pendown()
        painter.pensize(20)
        painter.dot(20, random.choice(real_colors))
        # painter.circle(10)
        # turtle.end_fill()
        painter.penup()


screen.exitonclick()