from tkinter import *
root=Tk()
def get_data(event=''):
    print('hi')
root.bind("<Control-t>",get_data)
main_menu=Menu(root)
root.config(menu=main_menu)
# creating File menu
filemenu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',accelerator='Ctrl+N',command=get_data)
filemenu.add_command(label='Open',accelerator='Ctrl+O')
filemenu.add_separator()
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')

# creating submenu
link_menu=Menu(filemenu,tearoff=0)
link_menu.add_command(label="Lf")
link_menu.add_command(label="CR")
filemenu.add_cascade(label='Link Seprator',menu=link_menu)

filemenu.add_command(label='Exit',command=exit)

# creating Edit menu
editmenu=Menu(main_menu)
main_menu.add_cascade(label='Edit')

btn=Button(root,text="Clickme",command=get_data)
#btn.pack()
root.geometry("600x500+200+100")
root.resizable(0,0)
root.mainloop()
