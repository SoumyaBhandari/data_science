from pymongo import MongoClient

conn = MongoClient(host = "localhost", port = 27017)
print(conn)
db=conn["new_db"]
#collection1=db["contacts"]
collection2=db["emplopee"]
# db.contacts.insert_one({"name":"ritu","age":43,"salary":100})
db.employee.insert_one({"id":"1aaa223"})

