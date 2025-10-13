from turtle import Turtle,Screen

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)


def slight_turn_left():
    tim.circle(radius=100, extent=22.5)


def clearscreen():
    # tim.reset()
    tim.home()
    tim.clear()

def turn_right():
    tim.right(22.5)

def turn_left():
    tim.left(22.5)

tim = Turtle()

screen = Screen()

screen.listen()
screen.onkey(key="c", fun = clearscreen)
# screen.onkey(key="space", fun = move_forward)
screen.onkeypress(key="w", fun = move_forward)
# screen.onkey(key="w"and "a", fun = slight_turn_left)
# screen.onkeypress(key="a", fun = turn_left)
screen.onkey(key="a", fun = turn_left)
screen.onkey(key="s", fun = move_backward)
# screen.onkeypress(key="d", fun = turn_right)
screen.onkey(key="d", fun = turn_right)
screen.onkeypress(key="r", fun = slight_turn_left)


screen.exitonclick()