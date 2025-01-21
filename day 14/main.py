import random
import os
from game_data import data
import art

def cleaning_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def options_info(option):
    return f"{option['name']}, a {option['description']}, from {option['country']}."


first_option = random.choice(data)
second_option = random.choice(data)

def play_game():
    keep_playing = True
    player_score = 0

    first_option = random.choice(data)
    second_option = random.choice(data)

    while keep_playing:
        cleaning_screen()
        print(art.logo)

        while first_option == second_option:
            second_option = random.choice(data)

        print(f"Compare A: {options_info(first_option)}")
        print(art.vs)
        print(f"Against B: {options_info(second_option)}")
        
        player_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if first_option['follower_count'] > second_option['follower_count']:
            more_followers = first_option
        else:
            more_followers = second_option

        if (player_answer == 'a' and first_option == more_followers) or \
            (player_answer == 'b' and second_option == more_followers):
            player_score += 1
            first_option = second_option
            second_option = random.choice(data)
        else:
            cleaning_screen()
            print(art.logo)     
            print(f"Sorry, that's wrong. Final score: {player_score}")
            keep_playing = False

play_game()