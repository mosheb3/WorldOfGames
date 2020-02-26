## Moshe Barazani
## Date: 04-02-2020

from Live import *
from GuessGame import guess_num
from MemoryGame import play
from CurrencyRouletteGame import play
from SevenBoom import seven_boom

games_name = ("Memory Game", "Guess Game", "Currency Roulette", "Seven Boom")
num_of_difficulties = 5
num_of_games = len(games_name)

gamer_name = get_gamer_name()
which_game2play = load_game(num_of_games)
print(which_game2play)

num_of_games_list = createList(num_of_games)

if (which_game2play in num_of_games_list):
    if (which_game2play == 1):
        get_difficulty = get_game_difficulty(games_name[which_game2play - 1], num_of_difficulties)
        play(get_difficulty)

    elif (which_game2play == 2):
        get_difficulty = get_game_difficulty(games_name[which_game2play - 1], num_of_difficulties)
        computer_num = guess_num(get_difficulty)

    elif (which_game2play == 3):
        play()

    elif (which_game2play == 4):
        seven_boom()

    else:
        print(games_name[which_game2play-1])

else:
    print("No Game Found")
