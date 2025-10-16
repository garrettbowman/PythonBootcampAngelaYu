import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move_up, "w")
index = 0
game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()
    index +=1
    for car in car_manager.cars:
        if car.distance(player) <15:
            scoreboard.game_over()
            screen.update()
            time.sleep(1)
            game_is_on = False
    if index % 5 ==0:
        car_manager.generate_car()
    if player.ycor() > 280:
        player.reset()
        car_manager.level_up()
        scoreboard.new_level()

    car_manager.move()
