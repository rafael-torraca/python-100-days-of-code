from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Score(Turtle):
    
    def __init__(self, ) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()



    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    
    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
