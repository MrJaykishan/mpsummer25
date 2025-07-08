from tkinter import *
from tkinter import ttk
root=Tk()
def get_data():
    if i.get()==1:
        print("Hindi")
    if j.get() == 1:
        print("English")
    if k.get() == 1:
        print("Urdu")
f=LabelFrame(root,text="Select Known Language")
f.pack()
i=IntVar()
j=IntVar()
k=IntVar()
c=Checkbutton(f,text="Hindi",variable=i)
c.pack()
c1=Checkbutton(f,text="English",variable=j)
c1.pack()
c1=Checkbutton(f,text="Urdu",variable=k)
c1.pack()
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
