## Moshe Barazani
## Date: 04-02-2020
## filename: MainGame.py
## pip install -r data/requirements.txt

from Live import *
from Utils import *
import json
from GuessGame import guess_num
from MemoryGame import play_memory_game
from CurrencyRouletteGame import play_currency_roulette
from SevenBoom import play_seven_boom
from Score import *
from datetime import datetime

now = datetime.now()
game_time = now.strftime("%m/%d/%Y %H:%M")
games_name = ("Memory Game", "Guess Game", "Currency Roulette", "Seven Boom")
num_of_difficulties = 5
ynq = "y"
new_game = "y"
num_of_games = len(games_name)

gamer_name = get_gamer_name()

##while (ynq.lower() == "y"):
while True:
    which_game2play = load_game(num_of_games)

    num_of_games_list = createList(num_of_games)
#    get_difficulty = get_game_difficulty(games_name[which_game2play - 1], num_of_difficulties)

    if (which_game2play in num_of_games_list):
        if (which_game2play in (1,2,3)):
            get_difficulty = get_game_difficulty(games_name[which_game2play - 1], num_of_difficulties)

        if (which_game2play == 1):
            game_score = play_memory_game(get_difficulty)

        elif (which_game2play == 2):
            game_score,computer_num = guess_num(get_difficulty)

        elif (which_game2play == 3):
            game_score = play_currency_roulette(get_difficulty)

        elif (which_game2play == 4):
            play_seven_boom()
        else:
            print(games_name[which_game2play-1])
    else:
        print("No Game Found")

    if (which_game2play != 4):
        scorePage = createGamerScoreTableBody(game_time, gamer_name, game_score, games_name[which_game2play-1])
        if (new_game == "n"):
            writeScore2File(SCORES_FILE_NAME, scorePage, "append")
        else:
            writeScore2File(SCORES_FILE_NAME, scorePage, "write")


    #call(["python", "webServer.py"])

    ## ynq = (input("Another Game? [y/n] "))
    ynq = input('Another Game? (Y/N) << ').lower()

    new_game = "n"

    while ynq.lower() not in ("y", "n"):
        print("y or n")
        ynq = input('Another Game? (Y/N) << ').lower()

    if (ynq.lower() == 'n'):
        with open('data/data.json', 'r') as handle:
            parsed = json.load(handle)
        exit()

    # if (ynq != "y" and ynq != "n"):
    #     ynq = None
    #     ynq = (input("Another Game? [y/n] ")).lower()
    #
    #if (ynq == "n"):
    #     exit()
#else:
#    ynq = (input("Another Game? [y/n] "))
