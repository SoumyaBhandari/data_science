import csv
file_object =open("hello.csv","w")
dw= csv.DictWriter(file_object,fieldnames=["name","age","salary"])
dw.writeheader()
filewriter=csv.writer(file_object,delimiter=',')
filewriter.writerow(["abc",28,545454])
filewriter.writerow(["dft",33,988888])
file_object.close()

