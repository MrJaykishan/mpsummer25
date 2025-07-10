from tkinter import *
from tkinter import filedialog,messagebox,colorchooser
from turtledemo.colormixer import setbgcolor

root=Tk()

def back():
    c=colorchooser.askcolor()
    t.config(background=c[1])
    print(c)
def fore():
    c = colorchooser.askcolor()
    t.config(foreground=c[1])
    print(c)


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
    d=filedialog.asksaveasfile(defaultextension=".txt",mode='w')
    print(d)
    data = t.get(1.0, END)
    d.write(data)



def new_file():
    x = t.get(1.0, END)
    if x.strip()=='':
        pass
    else:
        print(x)
        res = messagebox.askyesnocancel("Save File Confirmation", 'Do you want to Save this file?')
        if res==True:
            saveAs_file()
        elif res==False:
            t.delete(1.0, END)



t=Text(root,width=15,wrap=WORD,selectbackground='red')
# t.insert(INSERT,'hello how ar you\n')
# t.insert(INSERT,'i am fine')
# t.pack(fill=BOTH,expand=1)
t.pack()
btn_back=Button(root,text="background",command=back)
btn_back.pack()
btn_fore=Button(root,text="foreground",command=fore)
btn_fore.pack()
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
root.geometry("600x800+200+100")
# root.resizable(0,0)
root.mainloop()