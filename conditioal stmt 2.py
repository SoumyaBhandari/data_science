import random
a=int(input("enter value"))
random_no=random.randint(5,10)
jackpot_no=random.randint(5,10)
if a==random_no:
    if a==jackpot_no:
        print("u win and got jackpot")
elif a<5:
     print("number is small")
elif a>20:
     print("number is big")
else:
     print("better luck next time")