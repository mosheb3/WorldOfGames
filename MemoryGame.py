## Moshe Barazani
## Date: 25-02-2020

def generate_sequence(difficulty):
    import random

    max_num = 101
    mlist = random.sample(range(max_num), difficulty)
    print(mlist)

def start_up(difficulty):
    import time

    print("REMEMBER")
    sec = difficulty
    while( sec > 0):
        print(sec)
        sec -= 1
        time.sleep(1)
    print(" GO GO GO")
    cls()


def cls():
    print ('\n' * 25000)


def get_list_from_user():
    print("Did u remember the numbers? ")
    user_nums = input("Enter the number by delimiter \",\" :")
    print(user_nums)
    return


def is_list_equal():
    return


def play():
    return