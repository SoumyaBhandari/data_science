import random
chances=4
points=0
while chances>0:
    a=int(input("enter value"))
    random_no=random.randint(0,10)
    if a==random_no:
        print("u win and got jackpot")
        points+=10
        if points <= 0:
            points = 0
            print("Points: ", points)
        else:
            print("Points1: ", points)
    else:
        print("lose")
        points-=3
        if points<=0:
            points=0
            print("Points: ", points)
        else:
            print("Points1: ", points)
    chances-=1
print("final points:",points)