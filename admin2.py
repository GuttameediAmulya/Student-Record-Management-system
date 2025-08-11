#import libraries
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
import customtkinter as ctk

#function to define database
def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    #creating STUD_REGISTRATION table
    
#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen =Tk()
    #setting width and height for window
    display_screen.geometry("1600x1600")
    #setting title for window
    display_screen.title("Student Management System")
    global tree
    global SEARCH
    global id,name,contact,email,address,grade
    SEARCH = StringVar()
    id = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    address=StringVar()
    grade = StringVar()

    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen,bd=1,height=100)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    width=display_screen.winfo_screenwidth()
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen,bg="#01041a")
    LeftViewForm.configure(width=(width/4))
    LeftViewForm.pack_propagate(0)
    
    LeftViewForm.pack(expand=True,side=LEFT,fill="both")
    #mid frame for displaying students record
    MidViewForm = Frame(display_screen)
    MidViewForm.pack()
    MidViewForm.configure(width=3*(width/4))
    MidViewForm.pack_propagate(0)
    MidViewForm.pack(expand=True,side=LEFT,fill="both")
    #label for heading
    lbl_text = Label(TopViewForm, text="Student Management System", font=("bold", 30),bg="#01041a", width=600,fg="white")
    lbl_text.pack(fill=X)
    userimage=Image.open("man.png")
    adminlabel=ctk.CTkLabel(LeftViewForm,image=ctk.CTkImage(dark_image=userimage,light_image=userimage),text='ADMIN',text_color="white",compound=LEFT,font=('Arial',25,'bold'))
    adminlabel.pack(pady=20,fill=X)
    #creating registration form in first left frame
    addbutton=ctk.CTkButton(LeftViewForm,text="ADD STUDENTS",font=('Cosmic Sans MS',16),text_color='white',fg_color="#01041a",hover_color="green",command=add)
    addbutton.pack(side=TOP,padx=20,pady=15, fill=X)

    
    #creating view button
    btn_view = ctk.CTkButton(LeftViewForm, text="VIEW ALL", font=('Cosmic Sans MS',16),text_color='white',fg_color="#01041a",hover_color="green",command=DisplayData)
    btn_view.pack(side=TOP,padx=20,  fill=X)
    #creating reset button
    btn_reset = ctk.CTkButton(LeftViewForm, text="RESET",font=('Cosmic Sans MS',16),text_color='white',fg_color="#01041a",hover_color="green", command=Reset)
    btn_reset.pack(side=TOP,padx=20,pady=15, fill=X)
    #creating delete button
    btn_delete = ctk.CTkButton(LeftViewForm, text="DELETE",font=('Cosmic Sans MS',16),text_color='white',fg_color="#01041a",hover_color="red", command=Delete)
    btn_delete.pack(side=TOP,padx=20,  fill=X)
    
    #update button 
    btn_update = ctk.CTkButton(LeftViewForm, text="UPDATE",font=('Cosmic Sans MS',16),text_color='white',fg_color="#01041a",hover_color="orange",command=update)
    btn_update.pack(side=TOP,padx=20,pady=15, fill=X)
    
    
     #edit staff 
    staffbutton=ctk.CTkButton(LeftViewForm,text="EDIT STAFF",font=('Cosmic Sans MS',16),text_color='white',fg_color="#01041a",hover_color="green",command=staff)
    staffbutton.pack(side=TOP,padx=20,pady=80, fill=X)
   #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    #creating search label and entry in second frame
   
    lbl_txtsearch = Label(MidViewForm, text="Enter Name or ID to search in records", font=('verdana', 15,'bold'))
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(MidViewForm, textvariable=SEARCH, font=('verdana', 15), width=10,)
    search.pack(side=TOP, padx=300, fill=X)
    btn_search = Button(MidViewForm, text="Search",font="bold",bg="blue",fg="white", command=SearchRecord)
    btn_search.pack(side=TOP, padx=400, pady=10, fill=X)
    tree = ttk.Treeview(MidViewForm,columns=( "Id","Name", "Contact", "Email","Address","Grade"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
   
    #setting headings for the columns
    tree.heading('Id', text="Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Address',text="Address",anchor=W)
    tree.heading('Grade', text="Grade", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=50)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    
    
    
    tree.pack()
    DisplayData()

#funcyion for updating
def update():
    def update_data():
        Database()
        query='update STUD_REGISTRATION set STU_NAME=?, STU_CONTACT=?, STU_EMAIL=?,STU_ADDRESS=?,STU_GRADE=? where STU_ID=?'
        cursor.execute(query,(nameentry.get(),contactentry.get(),emailentry.get(),addressentry.get(),gradeentry.get(),identry.get()))
        conn.commit()
        tkMessageBox.showinfo("success","Data updated Successfully")
        up_window.destroy()
        DisplayData()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to update")
    else:
     up_window = Toplevel()
     up_window.title("update student details")    
     up_window.grab_set()
     up_window.resizable(False,False)
     idlabel=Label(up_window,text="id",font=("",12,"bold"))
     idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
     identry=Entry(up_window,font=("",12,"bold"),width=24)
     identry.grid(row=0,column=1,pady=15,padx=10)

     namelabel=Label(up_window,text="name",font=("",12,"bold"))
     namelabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
     nameentry=Entry(up_window,font=("",12,"bold"),width=24)
     nameentry.grid(row=1,column=1,pady=15,padx=10)

     contactlabel=Label(up_window,text="contact",font=("",12,"bold"))
     contactlabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
     contactentry=Entry(up_window,font=("",12,"bold"),width=24)
     contactentry.grid(row=2,column=1,pady=15,padx=10)

     emaillabel=Label(up_window,text="email",font=("",12,"bold"))
     emaillabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
     emailentry=Entry(up_window,font=("",12,"bold"),width=24)
     emailentry.grid(row=3,column=1,pady=15,padx=10)

     addresslabel=Label(up_window,text="address",font=("",12,"bold"))
     addresslabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
     addressentry=Entry(up_window,font=("",12,"bold"),width=24)
     addressentry.grid(row=4,column=1,pady=15,padx=10)

     gradelabel=Label(up_window,text="Grade",font=("",12,"bold"))
     gradelabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
     gradeentry=Entry(up_window,font=("",12,"bold"),width=24)
     gradeentry.grid(row=5,column=1,pady=15,padx=10)
    
     update_button=ctk.CTkButton(up_window,text="update",font=('Cosmic Sans MS',16),text_color='white',hover_color="orange",command=update_data)
     update_button.grid(row=6,column=2,pady=15)
    

    
   
     tree.selection()  
     curItem = tree.focus()
     contents = (tree.item(curItem))
     listdata=contents['values']
     identry.insert(0,listdata[0])
     nameentry.insert(0,listdata[1])
     contactentry.insert(0,listdata[2])
     emailentry.insert(0,listdata[3])
     addressentry.insert(0,listdata[4])
     gradeentry.insert(0,listdata[5])

def add():
     def register():
       Database()
    #getting form data
       id1=identry.get()
       name1=nameentry.get()
       contact1=contactentry.get()
       email1=emailentry.get()
       address1=addressentry.get()
       grade1=gradeentry.get()
    #applying empty validation
       if id1=='' or name1=='' or contact1==''or email1=='' or address1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
       else:
        #execute query
        conn.execute('INSERT INTO STUD_REGISTRATION (STU_ID,STU_NAME,STU_CONTACT,STU_EMAIL,STU_ADDRESS,STU_GRADE) \
              VALUES (?,?,?,?,?,?)',(id1,name1,contact1,email1,address1,grade1));
        conn.commit()
        add_window.destroy()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()

     add_window = Toplevel()
     add_window.title("add student details")    
     add_window.grab_set()
     add_window.resizable(False,False)
     idlabel=Label(add_window,text="id",font=("",12,"bold"))
     idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
     identry=Entry(add_window,font=("",12,"bold"),width=24)
     identry.grid(row=0,column=1,pady=15,padx=10)

     namelabel=Label(add_window,text="name",font=("",12,"bold"))
     namelabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
     nameentry=Entry(add_window,font=("",12,"bold"),width=24)
     nameentry.grid(row=1,column=1,pady=15,padx=10)

     contactlabel=Label(add_window,text="contact",font=("",12,"bold"))
     contactlabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
     contactentry=Entry(add_window,font=("",12,"bold"),width=24)
     contactentry.grid(row=2,column=1,pady=15,padx=10)

     emaillabel=Label(add_window,text="email",font=("",12,"bold"))
     emaillabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
     emailentry=Entry(add_window,font=("",12,"bold"),width=24)
     emailentry.grid(row=3,column=1,pady=15,padx=10)

     addresslabel=Label(add_window,text="address",font=("",12,"bold"))
     addresslabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
     addressentry=Entry(add_window,font=("",12,"bold"),width=24)
     addressentry.grid(row=4,column=1,pady=15,padx=10)

     gradelabel=Label(add_window,text="Grade",font=("",12,"bold"))
     gradelabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
     gradeentry=Entry(add_window,font=("",12,"bold"),width=24)
     gradeentry.grid(row=5,column=1,pady=15,padx=10)
    
     update_button=ctk.CTkButton(add_window,text="ADD",font=('Cosmic Sans MS',16),text_color='white',hover_color="green",command=register)
     update_button.grid(row=6,column=2,pady=15)
def staff():
    def addstaff():
         Database()
         sid1=sid.get()
         sname1=sname.get()
         if sid1=='' or sname1=='':
             tkMessageBox.showinfo("Warning","fill the empty field!!!") 
         else:
             conn.execute("insert into staff(id,name) values(?,?)",(sid1,sname1))
             conn.commit()
             tkMessageBox.showinfo("success","Teacher Added successfully")
             displaystaff()
             conn.close()
    def deletestaff():
        Database()
        if not tree.selection():
          tkMessageBox.showwarning("Warning","Select data to delete")
        else:
          result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to remove accss to this teacher?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM staff WHERE id= %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

    def displaystaff():
        
    #open database
     Database()
     #clear current data
     tree.delete(*tree.get_children())
    #select query
     cursor=conn.execute("SELECT * FROM staff")
    #fetch all data from database
     fetch = cursor.fetchall()
    #loop for displaying all data in GUI
     for data in fetch:
        tree.insert('', 'end', values=(data))
     
     cursor.close()
     conn.close()
        
    def resetstaff():
        sid.set("")
        sname.set("")


    
    s_window = Toplevel()
    s_window.title("update student details")    
    s_window.grab_set()
    
    global sid,sname
    sid= StringVar()
    sname= StringVar()
    TopViewForm = Frame(s_window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    lb2_text = Label(TopViewForm, text="STAFF DETAILS",bg="#01041a",fg="white", font=("bold", 30))
    lb2_text.pack(fill=X)
    
    LFrom = Frame(s_window, width="400",bg="#01041a")
    LFrom.pack(side=LEFT, fill=Y)
    Label(LFrom,text="Add a Teacher", font=("Arial", 15, "bold"),bg="#01041a", fg="white").pack(side=TOP,pady=20)
    sidlabel=Label(LFrom, text="ID", font=("Arial", 12),bg="#01041a",fg="white").pack(side=TOP)
    sidentry= Entry(LFrom, font=("Arial", 10, "bold"),textvariable=sid).pack(side=TOP, padx=10, fill=X)
    snamelabel=Label(LFrom, text="Name ", font=("Arial", 12),bg="#01041a",fg="white").pack(side=TOP)
    snameentry=Entry(LFrom,font=("Arial",10,"bold"),textvariable=sname).pack(side=TOP, padx=10, fill=X)
    
    addbutton=ctk.CTkButton(LFrom,text="ADD",font=('Cosmic Sans MS',16),text_color='white',bg_color="white",fg_color="#01041a",hover_color="green",command=addstaff)
    addbutton.pack(side=TOP,padx=25,pady=15, fill=X)

    #delete a staff
    Button(LFrom,text="Remove",font=("Arial", 10, "bold"),bg="red",command=deletestaff).pack(side=TOP, padx=10,pady=25, fill=X)

    #seconf left frame for search form
    LeftViewForm = Frame(s_window,bg="gray")
    LeftViewForm.pack(side=LEFT, fill=Y)
    tree = ttk.Treeview(LeftViewForm,columns=( "Id","Name"),
                        selectmode="extended", height=100,)
   
    #setting headings for the columns
    tree.heading('Id', text="Id/PASSWORD", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=10)
    tree.pack()
    displaystaff()



#function to insert data into database

def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    id.set("")
    name.set("")
    contact.set("")
    email.set("")
    address.set("")
    grade.set("")
    

def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID= %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


    
   


#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_NAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))

        cursor=conn.execute("SELECT * FROM STUD_REGISTRATION WHERE STU_ID LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))

    



#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM STUD_REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


    

#calling function
DisplayForm()
if __name__=='__main__':
 

#Running Application
 mainloop()
