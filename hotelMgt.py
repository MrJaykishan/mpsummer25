from tkinter import *
from tkinter import messagebox
import pymysql

from datbase_connectivity import mycursor

taz=Tk()
taz.title('Taz Hotel')
height=taz.winfo_screenheight()
#print(height)
width=taz.winfo_screenwidth()
#print(width)
def clear_screen():
    global taz
    for widgets in taz.winfo_children():
        widgets.grid_remove()
def dbconfig():
    global conn, mycursor
    conn=pymysql.connect(host="localhost",user="root",db="tazhotel")
    mycursor=conn.cursor()

def adminLogout():
    clear_screen()
    main_heading()
    loginwindow()
def adminLogin():
    if usernameVar.get()=='' or passwordVar.get()=='':
        messagebox.showerror("Error",'Please enter Both Entries')
    else:
        # print(usernameVar.get())
        # print(passwordVar.get())
        dbconfig()
        username = usernameVar.get()
        password = passwordVar.get()
        que = "select * from login_info where username=%s and password=%s"
        val = (username, password)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        print(data)
        flag = False
        for row in data:
            flag = True
        conn.close()

        if flag == True:
            welcomewindow()
            # messagebox.showwarning('','login successfull')
        else:
            messagebox.showerror("Invalid User Credential", "Either User Name or Password is Incorrect")
            usernameVar.set("")
            passwordVar.set("")
#main heading
def main_heading():
    label=Label(taz,text="Hotel Taz Management System",fg="red",bg="blue",
            font=("comic sans Ms",40,"bold"),padx=300,pady=0)
    label.grid(row=0,columnspan=4)

def additemprocess():
    if itemnameVar.get()=='' or itemtypeVar.get()=='' or itemrateVar.get()=='':
        messagebox.showerror('Data Validation Error','Please Fill All Details of Item')
    else:
        name=itemnameVar.get()
        type=itemtypeVar.get()
        rate=itemrateVar.get()
        dbconfig()
        queins = "insert into menu_item (name,rate,type) values(%s,%s,%s)"
        val = (name,rate,type)
        mycursor.execute(queins, val)
        conn.commit()
        messagebox.showinfo('Data Saved','Data Saved Successfully')

itemnameVar=StringVar()
itemrateVar=StringVar()
itemtypeVar=StringVar()
def addItemWindow():
    clear_screen()
    main_heading()
    backButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, command=welcomewindow)
    backButton.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
    labelmenu = Label(taz, text="Insert Menu Item", font=("ariel", 25, "bold"))
    labelmenu.grid(row=1, column=1, columnspan=2, padx=50, pady=10)
    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=1, column=2, columnspan=2, padx=20, pady=5)
    ##########################################
    itemnameLabel = Label(taz, text="Item Name", font=("ariel", 20, "bold"))
    itemnameLabel.grid(row=2, column=1, padx=20, pady=5)

    itemrateLabel = Label(taz, text="Item Rate (INR)", font=("ariel", 20, "bold"))
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemtypeLabel = Label(taz, text="Item Type", font=("ariel", 20, "bold"))
    itemtypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    # for validation
    # itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    # itemrateEntry.configure(validate="key", validatecommand=(callback2, "%P"))

    itemtypeEntry = Entry(taz, textvariable=itemtypeVar)
    itemtypeEntry.grid(row=4, column=2, padx=20, pady=5)
    # itemtypeEntry.configure(validate="key", validatecommand=(callback, "%P"))
    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=additemprocess)
    additemButton.grid(row=5, column=1, columnspan=2)

    #############################################
def billWindow():
    pass
usernameVar=StringVar()
passwordVar=StringVar()
def loginwindow():
    usernameVar.set("")
    passwordVar.set("")
    labellogin=Label(taz,text="Admin Login",font=("ariel",25,"bold"))
    labellogin.grid(row=1,column=1,columnspan=2,padx=50,pady=10)

    usernameLabel=Label(taz,text="User Name",font=("ariel",12,"bold"))
    usernameLabel.grid(row=2,column=1,padx=20,pady=5)

    passwordLabel = Label(taz, text="User Password",font=("ariel",12,"bold"))
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry=Entry(taz,textvariable=usernameVar)
    usernameEntry.grid(row=2,column=2,padx=20,pady=5)

    passwordEntry=Entry(taz,show="?",textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton=Button(taz,text="Login",width=20,height=2,fg="green",bd=10,command=adminLogin)
    loginButton.grid(row=4, column=1, columnspan=2,padx=20, pady=5)

# welcome window
def welcomewindow():
    clear_screen()
    main_heading()
    labelwelcome = Label(taz, text=" Welcome Admin ", font=("ariel", 25, "bold"))
    labelwelcome.grid(row=1, column=1, columnspan=2, padx=50, pady=10)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=adminLogout)
    logoutButton.grid(row=4, column=1, columnspan=2, padx=20, pady=5)

    manageRest = Button(taz, text="Manage Hotel", width=20, height=2, fg="green", bd=10, command=addItemWindow)
    manageRest.grid(row=5, column=1, columnspan=2, padx=20, pady=5)

    billGen = Button(taz, text="Bill Generation", width=20, height=2, fg="red", bd=10, command=billWindow)
    billGen.grid(row=6, column=1, columnspan=2, padx=20, pady=5)
main_heading()
loginwindow()
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()