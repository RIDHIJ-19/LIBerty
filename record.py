from tkinter import *
from tkinter import messagebox
import sqlite3
import calendar
from tkinter import *  # importing all methods, classes and widgets from the tkinter library
from PIL import ImageTk, Image  # importing the ImageTk and Image modules from the PIL library
import calendar  # importing the calendar module
from datetime import date  # importing the date module from the datetime library

con=sqlite3.connect('library.db')
cur=con.cursor()


class record(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("RECORD")

        self.resizable(False, False)
        ###############################Frames################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # bottom frame
        self.bottomFrame = Frame(self, height=600, bg='#708d8d')
        self.bottomFrame.pack(fill=X)
        # heading,image
        heading = Label(self.topFrame, text=' Fine', font=' arial 30 bold', fg="#51702c", bg='white')
        heading.place(x=210, y=60)

        ################################################entries and labels########3

        # member name
        self.lbl_name = Label(self.bottomFrame, text='Name:', font='arial 10 bold', bg="#c4b48c", fg="black")
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, 'PLEASE ENTER BOOK NAME')
        self.ent_name.place(x=150, y=45)

        # button
        button = Button(self.bottomFrame, text='CALCULATE', command=self.delmember, fg='white', bg="#51702c")
        button.place(x=270, y=200)

    def delmember(self):
        name = self.ent_name.get()
        phone = self.ent_phone.get()

        if name and phone != "":
            try:
                query = "DELETE FROM 'MEMBERS' (member_name,member_phone) VALUES(?,? )"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo("Success", "Successfully removed from database")
            except:
                messagebox.showerror("ERROR", "Can delete from database")

        else:
            messagebox.showerror("ERROR", "Fields cant be empty")




