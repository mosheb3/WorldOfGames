
def generate_number(difficulty):
    import random
    secret_number = random.randint(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    user_guess = input("Please, guess a number between 1 and {df}: ".format(df=difficulty))
    return user_guess

def guess_num(difficulty):
    user_guess = int(get_guess_from_user(difficulty))
    if (user_guess == 1 and difficulty == 1):
        print("Ohh Really?!")
        exit()
    else:
        computer_num = generate_number(difficulty)
        if (computer_num == user_guess):
            print("Good, You won!")
            print("I thought also about number {cn}".format(cn=computer_num))
        else:
            print("Sorry, You lose!")
            print("I thought about number {cn}".format(cn=computer_num))
        return str(computer_num)
