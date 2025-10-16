#NON OOP Version
from turtle import Turtle, Screen
import random
import time

def start_game():
    return True

# def turn_right():
#     current_direction = "r"
#
# def turn_left():
#     current_direction = "l"
#
# def turn_up():
#     current_direction = 'up'
#
# def turn_down():
#     current_direction = "down"

def update_score():
    score.reset()
    score.hideturtle()
    score.color("white")
    score.penup()

    score.setposition(-50, 250)
    score.write(f"Score: {snake_length - 3}", font=('Arial', 18, 'normal'))

def turn_right():
    square.setheading(0)

def turn_left():
    square.setheading(180)

def turn_up():
    square.setheading(90)

def turn_down():
    square.setheading(270)

def game_over():
    spot = square.pos()
    spots=[]
    for _ in squares:
        spots.append(_.pos())
    if abs(spot[0]) > 280:
        return True
    elif abs(spot[1]) > 280:
        return True
    elif spot in spots:
        return True
    else:
        return False

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")

squares = []
snake_length = 3
food_locations = []


score = Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.setposition(-50, 250)
score.write(f"Score: {snake_length -3}", font=('Arial', 18, 'normal'))

for init in range(60,200,20):
    food_locations.append(init)

for init in range(3):
    square = Turtle(shape="square")
    square.penup()
    square.speed("slow")
    square.setx(0+init *20)
    square.penup()
    squares.append(square)

food = Turtle(shape="square")
food.setposition(random.choice(food_locations),random.choice(food_locations))
food.color("green")

for each in squares:
    each.color("white")


over = False
screen.listen()
screen.tracer(0)
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(fun=turn_up, key="w")
screen.onkeypress(turn_down, "s")
current_direction = "r"
while not over:
    #Generate thing
    # for s in range(0, snake_length):

    goal = food.pos()
    first_square = squares[-1].pos()
    if goal == first_square:
        snake_length += 1
        update_score()

    first_square_head = squares[-1].heading()
    square = Turtle(shape="square")
    square.speed("slow")
    square.penup()
    square.setposition(first_square)
    square.setheading(first_square_head)
    square.forward(20)
    over = game_over()
    if over:
        print("GG")
        its_over=Turtle()
        its_over.color("RED")
        its_over.penup()
        its_over.hideturtle()
        its_over.setposition(-80, 0)
        its_over.write(f"GAME OVER", font=('Arial', 18, 'normal'))
        break

    # if current_direction == "r":
    #     square.setx(first_square[0]+20)
    # elif current_direction == "l":
    #     square.setx(first_square[0]-20)
    # elif current_direction == 'up':
    #     square.sety(first_square[1]+20)
    # elif current_direction == "down":
    #     square.sety(first_square[1]-20)
    square.color("white")
    squares.append(square)
    screen.update()
    time.sleep(0.1)
    squares[0].reset()
    if goal != first_square:
        del squares[0]
    else:
        food.reset()
        food.penup()
        food.setposition(random.choice(food_locations), random.choice(food_locations))
        food.color("green")



screen.exitonclick()

