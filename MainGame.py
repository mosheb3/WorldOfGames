## Moshe Barazani
## Date: 04-02-2020

from Live import *
from GuessGame import guess_num
from MemoryGame import play_memory_game
from CurrencyRouletteGame import play_currency_roulette
from SevenBoom import play_seven_boom

games_name = ("Memory Game", "Guess Game", "Currency Roulette", "Seven Boom")
num_of_difficulties = 5
ynq = "y"
num_of_games = len(games_name)

gamer_name = get_gamer_name()

while(ynq.lower() == "y"):
    which_game2play = load_game(num_of_games)

    num_of_games_list = createList(num_of_games)
#    get_difficulty = get_game_difficulty(games_name[which_game2play - 1], num_of_difficulties)

    if (which_game2play in num_of_games_list):
        if (which_game2play in (1,2,3)):
            get_difficulty = get_game_difficulty(games_name[which_game2play - 1], num_of_difficulties)

        if (which_game2play == 1):
            play_memory_game(get_difficulty)

        elif (which_game2play == 2):
            computer_num = guess_num(get_difficulty)

        elif (which_game2play == 3):
            play_currency_roulette(get_difficulty)

        elif (which_game2play == 4):
            play_seven_boom()

        else:
            print(games_name[which_game2play-1])

    else:
        print("No Game Found")

    ynq = (input("Another Game? [y/n] ")).lower()
else:
    exit()
