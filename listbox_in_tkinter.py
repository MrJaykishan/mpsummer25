from tkinter import *

root=Tk()
def get_data():
    pass
f=Frame(root)
f.pack()
sc=Scrollbar(f)
l=Listbox(f,height=10,width=15,selectmode=EXTENDED,
          yscrollcommand = sc.set)
#l.insert(END,'hifsdgsdgsdgsdgsgsgsdgsdgsgsgsdgsdgsdgsdgsdgsdgsdgsdg')
for i in range(15):
    l.insert(END,i)
l.pack(side=LEFT)

sc.pack(side=RIGHT,fill=Y)
sc.config(command = l.yview)
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
