from turtle import Screen, Turtle
from random import choice

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue", "red")

colours = ["red", "blue", "green"]

num_sides = 3

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.fd(50)
        timmy_the_turtle.right(angle)


for n in range(3, 11):
    timmy_the_turtle.color(choice(colours))
    draw_shape(n)
    

# for _ in range(4):
#     for _ in range(10):
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(10)
#         timmy_the_turtle.pendown()
#     timmy_the_turtle.right(90)

screen = Screen()

screen.exitonclick()