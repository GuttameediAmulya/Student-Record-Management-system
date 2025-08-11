import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
import os


# Function to validate the login
def login():
 if userentry.get()=="" or passwordentry.get()=="":
  messagebox.showerror('Error','Fields cannot be empty')
 elif userentry.get()=='admin' and passwordentry.get()=='admin@admin':
  messagebox.showinfo('success','WELCOME ADMIN')
 
  root.destroy()
  os.system('python admin2.py')
  #import admin2.py
  

 else: 
  checkinfo()
    
def checkinfo():
  conn = sqlite3.connect("student.db")
  cursor = conn.cursor()
  query="select * from staff where name=? and id=?"
  cursor.execute(query,(userentry.get(),passwordentry.get()))
  user=cursor.fetchone()
  if user:
    messagebox.showinfo('sucess','WELCOME TEACHER') 
    root.destroy()
    #import teacher.py
    os.system('python teacher.py')
  
  else:
     messagebox.showinfo('failed','ENTER VALID CREDENTIALS') 
  
  
# Create the main window
root= tk.Tk()
root.title("Login Form")
root.geometry("1200x1200+0+0")
root.resizable(False,False)

backgroundimage=ImageTk.PhotoImage(file='bg.jpg')
bg=Label(root,image=backgroundimage)
bg.place(x=0,y=0)

titleframe=Frame(root)
titleframe.place(x=300,y=50)
titlelabel=Label(titleframe,text="STUDENT MANAGEMENT SYSTEM",font=('','30','bold'))
titlelabel.grid(row=0)


loginframe=Frame(root)
loginframe.place(x=400,y=250) 



# Create and place the username label and entry
userimage=PhotoImage(file='user.png')
userlabel=Label(loginframe,image=userimage,text='USERNAME',compound=LEFT,font=('','20','bold'))
userlabel.grid(row=2,column=0,)

userentry=Entry(loginframe,font=('','20','bold'),bg="white")
userentry.grid(row=2,column=1)

passwordimage=PhotoImage(file='pass.png')
passwordlabel=Label(loginframe,image=passwordimage,text='PASSWORD',compound=LEFT,font=('','20','bold'))
passwordlabel.grid(row=3,column=0,pady=20)

passwordentry=Entry(loginframe,font=('','20','bold'),show="*")
passwordentry.grid(row=3,column=1,pady=20)

loginbutton=Button(loginframe,text='Login',font=('','15','bold'),width=15,fg="white",bg="cornflowerblue",command=login)
loginbutton.grid(row=4,column=1)


root.mainloop()