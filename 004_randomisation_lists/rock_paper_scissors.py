import random

player1 = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
)

computer = random.randint(0, 2)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options_list = [rock, paper, scissors]

print(f"Player 1 choose: \n{options_list[player1]}\n")
print(f"Computer choose: \n{options_list[computer]}\n")


if (
    (player1 == 0 and computer == 2)
    or (player1 == 1 and computer == 0)
    or (player1 == 2 and computer == 1)
):
    print("You win!")
elif (
    (computer == 0 and player1 == 2)
    or (computer == 1 and player1 == 0)
    or (computer == 2 and player1 == 1)
):
    print("You lose!")
elif player1 == computer:
    print("Draw")
else:
    print("Wrong choice!")
