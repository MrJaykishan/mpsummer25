from tkinter import *
root=Tk()

def msg():
    print("hello")
def test():
    print("hi")
root.title("calculator")
root.wm_iconbitmap('calci.ico')
# creating a button
btn=Button(root,text="Click Me",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=msg)
btn.pack(side='top',fill='x')

btn1=Button(root,text="Add",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=test)
btn1.pack(side='left',fill='y')

btn2=Button(root,text="Bottom",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"))
btn2.pack(side='bottom')

btn3=Button(root,text="Right",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"))
btn3.pack(side="right")


root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()