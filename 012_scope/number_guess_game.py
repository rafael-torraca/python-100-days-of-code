from random import randint
from os import system

EASY_GAME_TURNS = 10
HARD_GAME_TURNS = 5

system("clear || cls")

def game_level():
    level = input("Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_GAME_TURNS
    else:
        return HARD_GAME_TURNS


def generate_number():
    return randint(1,100)


def check_guess(user_guess, number, attempts):
    if user_guess > number:
        print("Too high.")
        return attempts - 1
    elif user_guess < number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The number is {number}")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = generate_number()
    attempts = game_level()
    print(number)
    user_guess = 0


    while user_guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        
        attempts = check_guess(user_guess, number, attempts)

        if attempts == 0:
            print(f"You lose! The number was {number}")
            return
        elif user_guess != number:
            print("Guess again.")

while input("Play again: 'y' or 'n': ") == 'y':
    system("clear || cls")
    game()

