from tkinter import *
import pymysql
#step1
conn = pymysql.connect(host='127.0.0.1',user='root',database='college')
print("connection established")
def get_data():
    name=x.get()
    age=int(y.get())
    print("Name=",name,"Age=",age)
    # step2
    mycursor = conn.cursor()
    # step3

    #sql_insert = "insert into student_info(name,age) values(%s,%s)"
    sql_update = "update student_info set name=%s,age=%s where name='abc'"
    #mycursor.execute( sql_insert,(name,age))
    mycursor.execute(sql_update, (age,name))
    conn.commit()





root=Tk()
root.title("My first window")

lbl=Label(root,text="Enter name",fg="red",bg="pink",
            font=("comic sans ms",15,'bold'))
lbl.place(x=10,y=50)
lbl12=Label(root,text="Enter age",fg="red",bg="pink",
            font=("comic sans ms",15,'bold'))
lbl12.place(x=10,y=150)

x=StringVar()
txt=Entry(root,fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=x)
txt.place(x=300,y=50)

y=StringVar()
txt=Entry(root,fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=y)
txt.place(x=300,y=150)

btn=Button(root,text="Save Data", fg="blue",bg="pink",
           font=("comic sans ms",15,'bold'),
           command=get_data)

btn.place(x=150,y=250)

result=StringVar()
lbl1=Label(root,fg="red",
            font=("comic sans ms",15,'bold'),textvariable=result)
lbl1.place(x=150,y=350)
root.geometry("650x600+500+200")
root.resizable(0,0)
root.mainloop()