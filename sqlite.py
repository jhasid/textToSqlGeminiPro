import sqlite3

# Connect to Sqlite db and create db if not exists it will create
connection=sqlite3.connect("student.db")

#Create a cursor object to insert record
cursor=connection.cursor()

#create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)   #create a table

#Insert some records
cursor.execute('''Insert into STUDENT values('RAM','AI','A')''')
cursor.execute('''Insert into STUDENT values('ABIRAM','AIOPS','B')''')
cursor.execute('''Insert into STUDENT values('Tom','AI','A')''')
cursor.execute('''Insert into STUDENT values('Mary','ML','C')''')
cursor.execute('''Insert into STUDENT values('Xi','ML','C')''')
 
 #Display all record

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)