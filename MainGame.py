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
from LoadScore import load_score_in_broser
from datetime import datetime

now = datetime.now()
game_time = now.strftime("%m/%d/%Y %H:%M")
games_name = ("Memory Game", "Guess Game", "Currency Roulette", "Seven Boom")
num_of_difficulties = 5
ynq = "y"
new_game = "y"
num_of_games = len(games_name)

gamer_name = get_gamer_name()

host_ip = get_host_ip()

while True:
    which_game2play = load_game(num_of_games)

    num_of_games_list = create_list(num_of_games)

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
        score_page = createGamerScoreTableBody(game_time, gamer_name, game_score, games_name[which_game2play-1])
        if (new_game == "n"):
            write_score_2_file(SCORES_FILE_NAME, score_page, "append")
        else:
            write_score_2_file(SCORES_FILE_NAME, score_page, "write")

    ynq = input('Another Game? (Y/N) << ').lower()

    new_game = "n"

    while ynq.lower() not in ("y", "n"):
        print("y or n")
        ynq = input('Another Game? (Y/N) << ').lower()

    if (ynq.lower() == 'n'):
        opr = get_operation_system()
        if (opr.lower() == "linux"):
           print("You can see your score at http://{h_ip}:8081".format(h_ip=host_ip))
        else:
           load_score_in_broser()
        exit()
