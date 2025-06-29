from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Scoreboard()
car_list = []
chance = 1
time_to_sleep = 0.1


screen.listen()
screen.onkey(key="Up", fun=player.move)

game_on = True
while game_on:
    screen.update()
    time.sleep(time_to_sleep)

    random_num = random.randint(1, 5)

    if chance == random_num:
        car = Cars()
        car_list.append(car)

    for car in car_list:
        car.move()
        #   Detect when turtle crashes with a car
        if player.distance(car) < 22:
            game_on = False
            level.game_over()

#   Detect when Turtle reaches the top
    if player.ycor() >= 290:
        player.reset()
        level.next_level()
        time_to_sleep *= 0.9



screen.exitonclick()