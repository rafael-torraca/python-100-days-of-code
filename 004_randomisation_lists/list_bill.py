import random

# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

names_string = input("Give me everybody's names, separated by a comma: \n")
names = names_string.split(", ")

list_lenght = len(names) - 1

random_choice = random.randint(0, list_lenght)
print(f"{names[random_choice]} is going to buy the meal today!")

# print(random.choice(names))
