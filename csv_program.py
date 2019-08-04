# read
import csv
name= []
age= []
sal= []
file_object= open("hello.csv", "r")
dictreader = csv.DictReader(file_object)
for row in dictreader:
    name.append(row['name'])
    age.append(row['age'])
    sal.append(row['salary'])
file_object.close()