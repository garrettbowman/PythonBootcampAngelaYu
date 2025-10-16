import turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle,Screen
import random

class CarManager:

    def __init__(self):
        self.car_speed = 0.1
        self.car_locations = []
        self.cars = []
        turtle.colormode(255)
        for x in range(-250, 250):
            self.car_locations.append(x)

    def generate_car(self):
        car = Turtle("square")
        car.speed("slow")
        car.penup()
        car.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, random.choice(self.car_locations))
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for x in self.cars:
            x.forward(MOVE_INCREMENT)

    def level_up(self):
        self.car_speed *= 0.8