from tkinter import *
from tkinter import ttk
root=Tk()
def get_data():
    print(i.get())
    if i.get()==1:
        print("Male")
    elif i.get()==2:
        print("female")

f=LabelFrame(root,text="Select Gender")
f.pack()
i=IntVar()
r1=Radiobutton(f,text="male",variable=i,value=1)
r1.pack()
r2=Radiobutton(f,text="female",variable=i,value=2)
r2.pack()
j=IntVar()
h1=Radiobutton(root,text="Ladka",variable=j,value=1)
h1.pack()
h2=Radiobutton(root,text="Ladki",variable=j,value=2)
h2.pack()
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
