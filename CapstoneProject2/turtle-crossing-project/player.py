from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(UP)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.setpos(STARTING_POSITION)
