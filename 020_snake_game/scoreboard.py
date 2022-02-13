from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
GAMEOVER_FONT = ("Courier", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore(self):
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")

    def read_highscore(self):
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())