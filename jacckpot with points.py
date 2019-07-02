import random
chance=4
while chance>0:
    a=int(input("enter value"))
    points=0
    random_no=random.randint(0,10)
    jackpot_no=random.randint(5,10)
    if a==random_no:
        if a==jackpot_no:
            print("u win and got jackpot")
            points=3
        elif a<5:
            print("number is small")
            points=4
    elif a>20:
            print("number is big")
            points=6
    else:
            print("better luck next time")
            points=8
    chance -= 1
print("ur points",points)

