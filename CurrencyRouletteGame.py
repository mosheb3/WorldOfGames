## Moshe Barazani
## Date: 04-02-2020
## using pip install python-exchangeratesapi
from Utils import *

def play_currency_roulette(difficulty):
    get_money_interval(difficulty)


def get_money_interval(difficulty):
    from exchangeratesapi import Api

    api = Api()
    d = difficulty
    user_num = get_guess_from_user()
    t = api.get_rate('USD', 'ILS')

    interval = (t - (5 - d), t + (5 - d))
    ## print(api.get_rate('USD', 'ILS'))

    r1 = interval[0]
    r2 = interval[1]

    if (user_num >= r1 and user_num <= r2):
        print("Good, You won!")
        return (WINNING_CODE)
    else:
        print("Sorry, You lose!")
        return (LOSSING_CODE)

def get_guess_from_user():
    user_guess = input("Please, guess a number between 1 and 100: ")
    return int(user_guess)

