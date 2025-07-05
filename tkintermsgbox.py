from tkinter import *
from tkinter import messagebox
root=Tk()
def get_data():
    # f=messagebox.askyesno("File Save Confirmation ","Do u want to save this file")
    f=messagebox.showerror()
    print(f)
    if f==True:
        print("File saved")
    else:
        exit()
btn=Button(root,text="open messagebox",fg="red",bg="yellow",
           font=("Comic Sans Ms",15,"bold"),command=get_data)
btn.place(x=150,y=250)

root.geometry("400x500+200+100")
root.resizable(0,0)
root.mainloop()