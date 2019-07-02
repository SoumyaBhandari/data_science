a=4
b=99
#static data
output="sum of" +str(a) +"and" +str(b) +"is"+ str(a+b)
output1="SUM OF{}AND{}IS{}".format(str(a),str(b),str(a+b))
print(output1)
#dynamic data
a=input("enter first no")
b=input("enter second no")
print(a,type(a))
print(b,type(b))
a=int(a)
b=int(b)
sum=a+b
print(sum)