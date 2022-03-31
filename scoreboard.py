from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-4, 270)
        self.color("white")
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

