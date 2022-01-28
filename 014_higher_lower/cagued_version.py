from art import logo, vs
from random import randint
from game_data import data
from os import system

system("cls || clear")
data_length = len(data)


def player_description(player):
    return f"{player['name']}, a {player['description']}, from {player['country']}."


def followers_comparation(player_one, player_two, score, end_game):
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    player_one_followers = player_one['follower_count']
    player_two_followers = player_two['follower_count']
    answer = "A" if player_one_followers > player_two_followers else "B"
    if answer == user_answer:
        return score + 1, end_game
    else:
        end_game = True
        return score, end_game


def start_game():
    end_game = False
    score = 0
    while not end_game:
        system("cls || clear")
        print(logo)
        if score > 0:
            print("You're right! Current score: {}".format(score))
        player_one_index = randint(0, data_length - 1)
        player_two_index = randint(0, data_length - 1)

        player_one_data = data[player_one_index]
        player_two_data = data[player_two_index]

        print(f"Compare A: {player_description(player_one_data)}")
        print(vs)
        print(f"Compare B: {player_description(player_two_data)}")

        score, end_game = followers_comparation(player_one_data, player_two_data, score, end_game)
    
    if end_game:
        system("cls || clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return

while input("Play again: 'y' or 'n': ") == 'y':
    system("clear || cls")
    start_game()
    