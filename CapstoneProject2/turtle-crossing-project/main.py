import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
Car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(Car.car_speed)
    screen.update()

    Car.create_car()
    for car in Car.CAR_LIST:
        car.forward(10)
        if player.distance(car) <= 22.36:
            game_is_on = False
            score.game_over()

    if player.ycor() == 280:
        score.new_score()
        player.restart()
        Car.new_speed()
    #
    # if player.distance(car) <= 22.36:
    #     game_is_on = False
    #     score.game_over()


screen.exitonclick()
