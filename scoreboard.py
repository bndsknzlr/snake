from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-4, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Courier New", 20, "normal"))

    def get_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
