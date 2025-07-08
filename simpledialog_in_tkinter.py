from tkinter import *
from tkinter import simpledialog

root=Tk()
def get_data():
    sum=0
    for i in range(5):
        a=simpledialog.askinteger('Marks Input',"Enter student Marks")
        print(a)
        sum=sum+a
        print("sum=",sum)

btn=Button(root,text="Clickme",command=get_data)
btn.pack()


root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
