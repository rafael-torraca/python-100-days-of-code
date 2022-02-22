# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
import csv
import turtle
from text import Text


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_csv_file(path: str):
    complete_data = []
    with open(path) as file:
        csv_data = csv.reader(file)
        for row in csv_data:
            complete_data.append(row)
        return complete_data




states = get_csv_file("50_states.csv")


game_is_on = True
while game_is_on:
    answer_state = screen.textinput("Guess the State", "What's another state's name?")
    formated_answer_state = answer_state.title()

    for state in states:
        if formated_answer_state == state[0]:
            name = state[0]
            cord_x = int(state[1])
            cord_y = int(state[2])
            new_state = Text(name, cord_x, cord_y)


# turtle.mainloop()

screen.exitonclick()
