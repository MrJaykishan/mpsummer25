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
l1.grid(row=0,column=0)
x=StringVar()
# x=IntVar()
text=Entry(root,justify='right',border="10",fg="red",font=("Comic Sans Ms",10,"bold"),textvariable=x)
text.grid(row=0,column=1)

# for second row
l11=Label(root,text="Enter Second Number",
         fg="red", bg="yellow",font=("Comic Sans Ms",10,"bold")
         )
l11.grid(row=1,column=0)
y=StringVar()
# x=IntVar()
text1=Entry(root,justify='right',border="10",fg="red",font=("Comic Sans Ms",10,"bold"),textvariable=y)
text1.grid(row=1,column=1)

# creating a button
btn=Button(root,text="Add",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=get_data)
btn.grid(row=2,column=0,columnspan=2)
#
btn_clear=Button(root,text="Clear",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=clear)
btn_clear.grid(row=3,column=0)
res=StringVar()
result=Label(root,fg="red", textvariable=res,font=("Comic Sans Ms",10,"bold")
         )
result.grid(row=3,column=1)

#root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()