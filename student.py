import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
from PIL import ImageTk
def select():
    if t1entry.get()=="":
      tkMessageBox.showwarning("warning","Student ID is required to search.")
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    query="SELECT * FROM STUD_REGISTRATION WHERE STU_ID=?"
    info=[t1entry.get()]
    cursor.execute(query,info)
    rows=cursor.fetchall()
    tree.config(height=10)   
    tree.delete(*tree.get_children())
    for items in rows:
        tree.insert("","end",values=(items))
    
root= tk.Tk()
root.title("STUDENT")
root.configure(bg="lightgrey")
root.geometry("1200x1200+0+0")

backgroundimage=ImageTk.PhotoImage(file='bg.jpg')
bg=Label(root,image=backgroundimage)
bg.place(x=0,y=0)



titleframe=Frame(root)
titleframe.place(x=200,y=150)
#titleframe.pack()
titlelabel=Label(titleframe,text="STUDENT MANAGEMENT SYSTEM",font=('','25','bold'))
titlelabel.grid(row=0,pady=20)

t1label=Label(titleframe,text="ENTER STUDENT ID",font=('','15','bold'),bg="lightgrey")
t1label.grid(row=2,column=0)

t1entry=Entry(titleframe,font=('','20','bold'),bg="white")
t1entry.grid(row=3)

subbutton=Button(titleframe,text="SUBMIT",width=30,bg="cornflowerblue",command=select)
subbutton.grid(row=4,pady=10)

#
tree = ttk.Treeview(titleframe,columns=( "Id","Name", "Contact", "Email","Address","Grade"),
                        selectmode="extended")

   
    #setting headings for the columns
tree.heading('Id', text="Id", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.heading('Address',text="Address",anchor=W)
tree.heading('Grade', text="Grade", anchor=W)
    #setting width of the columns
tree.column('#0', stretch=NO, minwidth=0, width=10)
tree.column('#1', stretch=NO, minwidth=0, width=100)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=100)
tree.column('#4', stretch=NO, minwidth=0, width=100)
    

    
tree.grid(row=5)


root.mainloop()