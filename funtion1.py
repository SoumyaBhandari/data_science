p=4000
r=8
t=input("time")
assert float(t),"plz provide value like 1 and 1.6"
if "." in t:
    t=float(t)
    si=(p*r*t)/100
else:
    t=int(t)
    si=(p*r*t)/100
print("Si",si)
