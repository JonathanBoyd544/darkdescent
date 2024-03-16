##### Rock Paper Scissors #####

import random

def get_choices():
    player_choice = input("Enter your choice (Rock, paper Scissors)\n>>> ")
    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)
    choices = {"player": player_choice, "computer": comp_choice}
    
    return choices

def check_win(player, computer):
    return [player, computer]

