
from tkinter import *
from tkinter import messagebox
import sqlite3
import adminlogin,userlogin

con = sqlite3.connect('library.db')
cur = con.cursor()


class login(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Delete Member")

        self.resizable(False, False)
        ###############################Frames################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # bottom frame
        self.bottomFrame = Frame(self, height=600, bg='#708d8d')
        self.bottomFrame.pack(fill=X)
        # heading,image
        heading = Label(self.topFrame, text="Login", font=' arial 30 bold', fg="#51702c", bg='white')
        heading.place(x=265, y=60)


        ################################################entries and labels########3



        # button
        button = Button(self.bottomFrame, text='User login', fg='white', bg="#51702c",font="comicsans 25 italic",
                        command=self.userlogin)
        button.place(x=250, y=100)
        button = Button(self.bottomFrame, text='Admin login',  fg='white', bg="#51702c",font="comicsans 25 italic",
                        command=self.adminlogin)
        button.place(x=250, y=200)



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
                messagebox.showinfo("welcome")

        else:
            messagebox.showerror("ERROR", "Fields cant be empty")

    def adminlogin(self):
        alog = adminlogin.adminlogin()
    def userlogin(self):
        alog = userlogin.userlogin()

