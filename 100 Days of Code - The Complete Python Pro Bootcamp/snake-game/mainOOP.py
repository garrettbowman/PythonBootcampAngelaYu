#OOP Version
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from scoreboard import Scoreboard



screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")
food_locations = []
score_board = Scoreboard()
snake = Snake()

for init in range(60,200,20):
    food_locations.append(init)


food = Turtle(shape="square")
food.setposition(random.choice(food_locations),random.choice(food_locations))
food.color("green")


over = False
screen.listen()
screen.tracer(0)
screen.onkeypress(snake.turn_left, "a")
screen.onkeypress(snake.turn_right, "d")
screen.onkeypress(fun=snake.turn_up, key="w")
screen.onkeypress(snake.turn_down, "s")

while not over:

    snake.move()
    goal = food.pos()

    if goal == snake.first_square:
        snake.snake_length += 1
        score_board.update_score()
        food.reset()
        food.penup()
        food.setposition(random.choice(food_locations), random.choice(food_locations))
        food.color("green")

    over = snake.game_over()
    if over:
        print("GG")
        its_over=Turtle()
        its_over.color("RED")
        its_over.penup()
        its_over.hideturtle()
        its_over.setposition(-80, 0)
        its_over.write(f"GAME OVER", font=('Arial', 18, 'normal'))
        break

    screen.update()
    time.sleep(0.1)





screen.exitonclick()

