import random
a=int(input("enter value"))
random_no=random.randint(0,10)
if a==random_no:
    print("u win")
elif a<5:
     print("number is small")
elif a>20:
     print("number is big")
else:
     print("better luck next time",a)