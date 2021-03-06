## Moshe Barazani
## Date: 04-02-2020
## filename: Live.py
import Utils

def get_gamer_name():
    gamer_name = input(Utils.blue + "Welcome, enter your name: ")
    print(Utils.blue + "\nHello {gn} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n".format(gn=gamer_name))
    return gamer_name


def load_game(num_of_games):
    print(Utils.green + "Please choose a game to play:\n \
   1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n \
   2. Guess Game - guess a number and see if you chose like the computer\n \
   3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n \
   4. Seven Boom \n" + Utils.white)

    game2play = ""
    game2play = input("Choose your game: ")
    num_of_games_list = create_list(num_of_games)

    if (game2play.isdigit()):
        while (int(game2play) not in num_of_games_list):
            game2play = input("Choose your game (1-" + str(num_of_games) + "): ")
    else:
        print("Only numbers allowed\n")
        game2play = load_game(num_of_games)

    return int(game2play)


def get_game_difficulty(game_name, num_of_difficulties):
    num_of_difficulties_list = create_list(num_of_difficulties)
    game_difficulty = input("Please choose game difficulty for \"{gn}\" from 1 to 5: ".format(gn=game_name))

    while not game_difficulty.isdigit():
        game_difficulty = input("Please choose game difficulty for \"{gn}\" from 1 to 5: ".format(gn=game_name))

    while (int(game_difficulty) not in num_of_difficulties_list):
        game_difficulty = input("Choose game difficulty (1-" + str(num_of_difficulties) + "): ")

    return int(game_difficulty)


def create_list(list_size):
    my_list = []
    for i in range(1, list_size+1):
        my_list.append(i)
    return my_list