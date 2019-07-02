a={"name":"ABC","age":32,"address":{"pin":7477,"city":"bhopal"},"hobby":["afcat","gre","cds"]}
print(a["name"])
a["name"]="ANAND"
a["age"]=31
a["hobby"][0]="IAS"
a["profession"]="teacher"
print(a)
del a["address"]["pin"]
print(a)
#FUNCTIONS OF DICT
print(a.keys())
#dict to list
print(list(a.keys()))
#function values
print(list(a.values()))
a["name"]=None
print(a)
b={1:"tanu",2:"soumya",3:"bhandari"}
a["name"]=b[1]
a.update(b)
print(a)
#values=None
b=dict.fromkeys(a,)
print(b)
print(b.items())
