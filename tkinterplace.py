from tkinter import *
root=Tk()
def get_data():
    # print(x.get())
    a=int(x.get())
    b=int(y.get())
    c=a+b
    # print(c)
    res.set(c)


def clear():
    x.set('')
    y.set('')
l1=Label(root,text="Enter First Number",
         fg="red", bg="yellow",font=("Comic Sans Ms",10,"bold")
         )
l1.place(x=10,y=50)
x=StringVar()
# x=IntVar()
text=Entry(root,justify='right',border="10",fg="red",font=("Comic Sans Ms",10,"bold"),textvariable=x)
text.place(x=200,y=50)

# for second row
l11=Label(root,text="Enter Second Number",
         fg="red", bg="yellow",font=("Comic Sans Ms",10,"bold")
         )
l11.place(x=10,y=150)
y=StringVar()
# x=IntVar()
text1=Entry(root,justify='right',border="10",fg="red",font=("Comic Sans Ms",10,"bold"),textvariable=y)
text1.place(x=200,y=150)

# creating a button
btn=Button(root,text="Add",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=get_data)
btn.place(x=150,y=250)

btn_clear=Button(root,text="Clear",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=clear)
btn_clear.place(x=300,y=250)
res=StringVar()
result=Label(root,fg="red", textvariable=res,font=("Comic Sans Ms",10,"bold")
         )
result.place(x=150,y=350)

root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()