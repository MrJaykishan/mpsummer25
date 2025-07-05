from tkinter import *
root=Tk()
def left_click(event):
    print("Left buton is clicked")

def middle_click(event):
    print("middle buton is clicked")
def right_click(event):
    print("right buton is clicked")
# creating a button
btn_left=Button(root,text="Left Click",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"))
btn_left.pack()

btn_right=Button(root,text="Right Click",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"))
btn_right.pack()

btn_middle=Button(root,text="Middle click",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"))
btn_middle.pack()

btn_left.bind("<Button-1>",left_click)
btn_middle.bind("<Button-2>",middle_click)
btn_right.bind("<Button-3>",right_click)
#for shortcutkey
root.bind("<Control-l>",left_click)
root.bind("<Control-m>",middle_click)
root.bind("<Control-r>",right_click)
root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()