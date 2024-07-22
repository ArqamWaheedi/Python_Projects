from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.Level = 0
        self.penup()
        self.hideturtle()
        self.new_score()

    def new_score(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.Level}", align="left", font=FONT)
        self.Level += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
