from turtle import Turtle

FONT = ("Courier", 14, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def point(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)