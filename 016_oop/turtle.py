# from turtle import Turtle, Screen
#
# timmy = Turtle()
# tommy = Turtle()
# # print(timmy)
# timmy.shape("turtle")
# timmy.color("green", "aquamarine")
# timmy.fd(125)
# timmy.rt(45)
# timmy.fd(100)
#
# tommy.fd(150)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

print(table.align)
table.align = "l"
print(table)
