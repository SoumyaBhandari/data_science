#create table

import sqlite3
conn=sqlite3.connect('hello database.db')
print(conn)
cursor=conn.cursor()
# query1="""CREATE TABLE lnt_emp(ID INT, NAME INT, AGE INT, SALARY INT)"""
# cursor.execute(query1)
# conn.commit()
# cursor.close()
# cursor.close()

# UPDATE
query1= "DELETE FROM lnt_emp WHERE ID=2"
query2="SELECT *FROM lnt_emp"
cursor.execute(query1)
cursor.execute(query2)
output=cursor.fetchall()
for i in output:
    print(i)

conn.commit()
cursor.close()


# #
# # # DELETE
# # query1="""UPDATE TABLE lnt_emp SET SALARY=75000 WHERE ID=1"""
# # cursor.execute(query1)
# # conn.commit()
# # cusror.close()
# #
# # # DATA QUERY LANGAUGE
# # query1="""SELECT ID,SALARY FROM lnt_emp WHERE SALARY>80000"""
# # cursor.execute(query1)
# # output=cursor.fetchall()
# # for i in output:
#     print(i)