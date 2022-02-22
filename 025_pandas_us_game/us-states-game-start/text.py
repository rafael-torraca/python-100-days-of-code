from turtle import Turtle

class Text(Turtle):

    def __init__(self, name, cor_x, cor_y):
        super(Text, self).__init__()
        self.name = name
        self.hideturtle()
        self.penup()
        self.goto(cor_x, cor_y)
        self.write(f"{self.name}")
