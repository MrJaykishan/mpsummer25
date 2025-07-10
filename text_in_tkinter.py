from tkinter import *
from tkinter import filedialog,messagebox
root=Tk()

def new_file():
    val = t.get(1.0, END)
    print(val)
    if val :
        print("Kuch likha nahi hi")
    else:
        print(val)
        print('kuch likha hi')


def get_data():
    print(t.get(1.0,END))
def open_file():
    global current_open_file
    f=filedialog.askopenfile(initialdir="/",
                               filetypes=[('All Files','*.*'),('Text File','*.txt')])
    current_open_file=f
    print(f)
    for data in f:
        t.insert(INSERT,data)

def save_file():
    s=open(current_open_file.name,'w')
    data=t.get(1.0,END)
    s.write(data)

def saveAs_file():
    d=filedialog.asksaveasfilename(defaultextension="*.txt")
    print(d)
t=Text(root,width=15,wrap=WORD,selectbackground='red')
# t.insert(INSERT,'hello how ar you\n')
# t.insert(INSERT,'i am fine')
# t.pack(fill=BOTH,expand=1)
t.pack()
btn_new=Button(root,text="new",command=new_file)
btn_new.pack()
btn=Button(root,text="Clickme",command=get_data)
btn.pack()
btn1=Button(root,text="open file",command=open_file)
btn1.pack()

btn_save=Button(root,text="Save file",command=save_file)
btn_save.pack()

btn_saveAs=Button(root,text="Save AS file",command=saveAs_file)
btn_saveAs.pack()
root.geometry("600x500+200+100")
# root.resizable(0,0)
root.mainloop()