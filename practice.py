def greet(name,msg):
   """This function greets to
   the person with the provided message"""
   print("Hello",name + ', ' + msg)

print(greet.__doc__)
greet("Good morning!","kk")