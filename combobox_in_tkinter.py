from tkinter import *
from tkinter import ttk
root=Tk()
dat=[]
for i in range(1,32):
    dat.append(i)
def get_data():
    print(c.get())
l=['ap','mp','up']
c=ttk.Combobox(root,value=dat)
c.set('Select Your state')
c.pack()
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
