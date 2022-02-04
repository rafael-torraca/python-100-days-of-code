from turtle import Turtle, Screen, turtles
from os import system
import random

system("cls || clear")


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]



# y_position = [-70, -40, -10, 20, 50, 80]

# for t_index in range(6):
#     tim = Turtle(shape="turtle")
#     tim.color(colors[t_index])
#     tim.penup()
#     tim.goto(x=-230, y=y_position[t_index])

all_turtles = []

y_position = -70
for t in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_ in all_turtles:
        if turtle_.xcor() > 210:
            is_race_on = False
            winning_color = turtle_.pencolor()
            if winning_color == user_bet:
                print("You've won! The {} turtle is winner!".format(winning_color))
            else:
                print("You've lost! The {} turtle is winner!".format(winning_color))
                
        rand_distance = random.randint(0, 10)
        turtle_.forward(rand_distance)

screen.exitonclick()

# criar classe