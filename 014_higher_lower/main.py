from art import logo, vs
from game_data import data
from random import choice
from os import system


def get_random_account():
    return choice(data)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    answer = "a" if a_followers > b_followers else "b"
    return guess == answer


def start_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = get_random_account()

    while game_should_continue:

        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        system("cls || clear")
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


while input('Start Game? "Y/N": ') == "y":
    system("cls || clear")
    start_game()
