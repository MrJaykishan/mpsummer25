from tkinter import *
from tkinter import filedialog
root=Tk()
def get_data():
    print(t.get(1.0,END))
def open_file():
    f=filedialog.askopenfile(initialdir="/",
                               filetypes=[('All Files','*.*'),('Text File','*.txt')])
    print(f)
    for data in f:
        t.insert(INSERT,data)
t=Text(root,bg="yellow")
t.insert(INSERT,'hello how ar you\n')
t.insert(INSERT,'i am fine')
# t.pack(fill=BOTH,expand=1)
t.pack()
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
btn1=Button(root,text="open file",command=open_file)
btn1.pack()
root.geometry("600x500+200+100")
# root.resizable(0,0)
root.mainloop()