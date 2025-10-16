from turtle import Turtle
import random
import time
from snake import Snake
from scoreboard import Scoreboard

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_locations = []
        # for init in range(60, 200, 20):
        #     self.food_locations.append(init)
        random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        # self.setposition(random.choice(self.food_locations), random.choice(self.food_locations))
        self.color("green")
        self.food_spot = self.pos()

    def change(self):
        self.penup()
        # self.setposition(random.choice(self.food_locations), random.choice(self.food_locations))
        random_x = random.randint(-220, 220)
        random_y = random.randint(-220, 220)
        self.goto(random_x, random_y)
        self.color("green")
        self.food_spot = self.pos()