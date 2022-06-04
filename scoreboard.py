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
        self.high_score = self.get_high_score()
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_high_score.txt", mode="w") as score_record:
                score_record.write(str(self.score))
        self.score = 0
        with open("my_high_score.txt") as score_record:
            self.high_score = int(score_record.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open("my_high_score.txt") as score_record:
            self.high_score = int(score_record.read())
            return self.high_score
