import tkinter as tk
from tkinter import *

from tkinter import messagebox
from PIL import ImageTk
import os

def admin():
    root.destroy()
    os.system('python login.py')

    
def teacher():
    root.destroy()
    os.system('python login.py')
   
def student():
    root.destroy()
    os.system('python student.py')
   
    
          
root= tk.Tk()
root.title("Student management Portal")
root.geometry("1200x1200+0+0")
root.resizable(False,False)

backgroundimage=ImageTk.PhotoImage(file='bg.jpg')
bg=Label(root,image=backgroundimage)
bg.place(x=0,y=0)

titleframe=Frame(root)
titleframe.place(x=300,y=50)
titlelabel=Label(titleframe,text="STUDENT MANAGEMENT SYSTEM",font=('','30','bold'))
titlelabel.grid(row=0)

homeframe=Frame(root)
homeframe.place(x=500,y=200)

loginbutton=Button(homeframe,text='ADMIN',font=('','15','bold'),width=15,fg="white",bg="cornflowerblue",command=admin)
loginbutton.grid(row=1,column=1,pady=10)
loginbutton=Button(homeframe,text='TEACHER',font=('','15','bold'),width=15,fg="white",bg="cornflowerblue",command=teacher)
loginbutton.grid(row=2,column=1,pady=10)
loginbutton=Button(homeframe,text='STUDENT',font=('','15','bold'),width=15,fg="white",bg="cornflowerblue",command=student)
loginbutton.grid(row=3,column=1,pady=10)

root.mainloop()