## Moshe Barazani
## Date: 04-02-2020

def seven_boom():
    num = int(input("Enter Number: "))
    for x in range(num):
        x+=1
        if not (x % 7):
            print("BOOM!")
        else:
            if "7" in str(x):
                print("BOOM!")
            else:
                print(x)