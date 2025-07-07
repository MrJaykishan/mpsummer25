from tkinter import *
root=Tk()
def open_msg(event=''):
    print("hi")
btn_left=Button(root,text="Btn Click",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=open_msg)
btn_left.pack()


#for shortcutkey

root.bind("<Control-r>",open_msg)
root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()