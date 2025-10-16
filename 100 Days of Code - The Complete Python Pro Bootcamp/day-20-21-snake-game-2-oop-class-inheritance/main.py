#OOP Version
from turtle import Turtle, Screen
import random
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My snake game")

food = Food()
score_board = Scoreboard()
snake = Snake()

over = False
screen.listen()
screen.tracer(0)
screen.onkeypress(snake.turn_left, "a")
screen.onkeypress(snake.turn_right, "d")
screen.onkeypress(fun=snake.turn_up, key="w")
screen.onkeypress(snake.turn_down, "s")

while not over:

    time.sleep(0.1)
    screen.update()

    goal = food.pos()
    over = snake.game_over()
    snake.move()

    if over:
        score_board.game_over()
        break

    if snake.head.distance(food) <= 20:
        snake.extend()
        score_board.update_score(snake.snake_length)
        food.change()

screen.exitonclick()

