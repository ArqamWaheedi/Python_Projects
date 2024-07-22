from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_speed = 0.1
        self.CAR_LIST = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            tim = Turtle()
            tim.shape("square")
            tim.penup()
            tim.setheading(180)
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.color(random.choice(COLORS))
            tim.goto(x=320, y=random.randint(-260, 260))
            self.CAR_LIST.append(tim)

    # def move(self):
    #     self.color(random.choice(COLORS))
    #     self.goto(x=320, y=random.randint(-260, 260))

    # def run(self):
    #     self.forward(MOVE_INCREMENT)

    def new_speed(self):
        self.car_speed *= 0.9
