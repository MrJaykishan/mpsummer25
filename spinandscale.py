from tkinter import *
root=Tk()
def get_data():
    print(s.get())
    print(sc.get())

s=Spinbox(root,from_=1,to=5)
s.pack()
sc=Scale(root,orient=HORIZONTAL,
         sliderlength=100,from_=100,to=500,length=300,width=30,bg='blue')
sc.set(250)
sc.pack()
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
