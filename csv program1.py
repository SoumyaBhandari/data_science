# write

import csv
import csv_program
row =["name","age","salary","hike","net salary"]
file_object1 = open("hello1.csv","a")
writer = csv.writer(file_object1)
writer.writerow(row)
for i in range(1,len(csv_program.sal)):
    writer.writerow([csv_program.name[i], csv_program.age[i],csv_program.sal[i], "10%",int((csv_program.sal[i]))+int(csv_program.sal[i])*0.1])
file_object1.close()