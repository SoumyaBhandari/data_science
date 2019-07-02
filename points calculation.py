#import random
chances=4
points=0
while chances>0:
    a=int(input("enter value"))
    random_no=10
    if a==random_no:
        points += 10
        print("u win and got jackpot")
        if points <= 0:
            points = 0
            print("Points: ", points)
        else:
            print("Points1: ", points)
    else:
        points -= 3
        print("lose")
        if points <= 0:
            points = 0
            print("Points: ", points)
        else:
            print("Points1: ", points)
    chances-=1
print("final points",points)

