from tkinter import *
root=Tk()

class MyWindow:
    def msg(self):
        print("hi")
    def __init__(self,master):
        self.master=master
        self.btn=Button(master,text="Clickme",command=self.msg)
        self.btn.pack()

ob=MyWindow(root)
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
