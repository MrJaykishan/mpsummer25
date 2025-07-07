from tkinter import *
from PIL import Image,ImageTk

root=Tk()

doc=ImageTk.PhotoImage(Image.open('images/doctor.png'))
btn_image=ImageTk.PhotoImage(Image.open('images/logout.png'))
def open_msg(event=''):
    print("hi")

l=Label(root,text="Doctor",image=doc,compound=BOTTOM,font=("Comic Sans Ms",15,"bold"))
l.grid(row=0,column=0)
btn_left=Button(root,image=btn_image,fg="red",
           font=("Comic Sans Ms",15,"bold"),command=open_msg)
btn_left.grid(row=6,column=0)


#for shortcutkey

root.bind("<Control-r>",open_msg)
root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()