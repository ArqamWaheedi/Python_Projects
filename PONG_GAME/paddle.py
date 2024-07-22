from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, a):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(a, 0)

    # def create_paddle(self):
    #     for pos in self.STARTING_POSITIONS:
    #         self.add_segment(pos)
    #
    # def add_segment(self, pos):
    #     new_turtle = Turtle("square")
    #     new_turtle.color("white")
    #     new_turtle.penup()
    #     new_turtle.goto(pos)
    #     self.segments.append(new_turtle)
    #
    # def move(self):
    #     for seg_num in range(len(self.segments) - 1, 0, -1):
    #         new_x = 380
    #         new_y = self.segments[seg_num - 1].ycor()
    #         self.segments[seg_num].goto(new_x, new_y)
    #     self.segments[0].setheading(90)
    #     self.segments[0].forward(20)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
