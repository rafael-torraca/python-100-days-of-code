from turtle import Screen, Turtle
from random import choice, randint
import turtle

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# for _ in range(36):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.rt(10)

screen = Screen()

screen.exitonclick()
