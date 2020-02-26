## Moshe Barazani
## Date: 25-02-2020

def generate_sequence(difficulty):
    import random

    max_num = 101
    gslist = random.sample(range(max_num), difficulty)
    print(gslist)
    return gslist


def start_up(difficulty):
    import time

    sec = difficulty
    while( sec > 0):
        print(sec)
        sec -= 1
        time.sleep(1)
    print(" GO GO GO")
    cls()


def cls():
    print ('\n' * 25000)


def get_list_from_user(difficulty):
    user_nums_list = []
    print("Did u remember the numbers? ")

    for i in range(difficulty):
        user_nums = input("Enter number {n}: ".format(n=i+1))
        user_nums_list.append(int(user_nums))
    #print(user_nums_list)
    return user_nums_list


def is_list_equal(gen_seq_list, gamer_num_list):
    if (gen_seq_list == gamer_num_list):
        print("Very Good! You'he good memory.")
    else:
        print("Sorry, The numbers was: {gen}".format(gen=gen_seq_list))
    return


def play(difficulty):
    gen_seq_list = []
    gamer_numbers = []
    print("REMEMBER")
    gen_seq_list = generate_sequence(difficulty)
    start_up(difficulty)
    gamer_numbers = get_list_from_user(difficulty)
    is_list_equal(gen_seq_list, gamer_numbers)
    return