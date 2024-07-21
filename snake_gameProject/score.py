from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score : {self.score} ", align="center", font=("Arial", 24, "normal"))
        self.ht()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.highscore} ", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
