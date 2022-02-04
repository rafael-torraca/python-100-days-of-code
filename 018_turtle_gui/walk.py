from turtle import Screen, Turtle
from random import choice, randint
import turtle

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed(0)
tim.pensize(15)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.fd(30)
    tim.setheading(choice(directions)) 

screen = Screen()

screen.exitonclick()