import pymysql
#step1
conn = pymysql.connect(host='127.0.0.1',user='root',database='college')
print("connection established")

#step2
mycursor=conn.cursor()

#step3
#sql_create="create table student_info(name varchar(25), age int(3))"
#sql_insert="insert into student_info(name,age) values('ram',25)"
sql_update="update student_info set name='shyam' where name='ram'"
#step4
mycursor.execute(sql_update)
conn.commit() # data ko save karne ke liy likhna na bhooole
#print("Table created successfully")
#print("Data inserted successfully")
print("Data updated successfully")
#step5
conn.close()
