## Moshe Barazani
## Date: 04-02-2020

def play_seven_boom():
    num = input("Enter Number: ")
    while not num.isdigit():
        num = input("Enter Number: ")

    for x in range(int(num)):
        x+=1
        if not (x % 7):
            print("BOOM!")
        else:
            if "7" in str(x):
                print("BOOM!")
            else:
                print(x)