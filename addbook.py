from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add Book")
        self.resizable(False, False)
        ###############################Frames################

        # Top Frame
        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)
        # bottom frame
        self.bottomFrame = Frame(self, height=600, bg='#708d8d')
        self.bottomFrame.pack(fill=X)
        # heading,image
        heading = Label(self.topFrame, text=' ADD BOOK', font=' arial 30 bold', fg="#51702c", bg='white')
        heading.place(x=230, y=60)


        ################################################entries and labels########3

        #name
        self.lbl_name=Label(self.bottomFrame,text='Name:',font='arial 10 bold',bg="#c4b48c",fg="black")
        self.lbl_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,'PLEASE ENTER A BOOK NAME')
        self.ent_name.place(x=150,y=45)
        ##author
        self.lbl_author = Label(self.bottomFrame, text=' Author:', font='arial 10 bold',bg="#c4b48c",fg="black")
        self.lbl_author.place(x=40, y=80)
        self.ent_author = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_author.insert(0, 'PLEASE ENTER A  AUTHOR NAME')
        self.ent_author.place(x=150, y=85)
        ##page
        self.lbl_page = Label(self.bottomFrame, text='PAGE:', font='arial 10 bold',bg="#c4b48c",fg="black")
        self.lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_page.insert(0, 'PLEASE ENTER PAGE SIZE')
        self.ent_page.place(x=150, y=125)
        ##language
        self.lbl_language = Label(self.bottomFrame, text='LANGUAGE:', font='arial 10 bold', bg="#c4b48c",fg="black")
        self.lbl_language.place(x=40, y=160)
        self.ent_language = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_language.insert(0, 'PLEASE ENTER LANGUAGE')
        self.ent_language.place(x=150, y=165)
        #BUTTON
        button=Button(self.bottomFrame,text='Add Book',command=self.addBook,fg='white',bg="#51702c")
        button.place(x=270,y=200)
    def addBook(self):
        name= self.ent_name.get()
        author=self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if name and author and page and language != "":
            try:
                query="INSERT INTO 'books' (book_name,book_author,book_page,book_language) VALUES(?,?,?,?)"
                cur.execute(query,(name,author,page,language))
                con.commit()
                messagebox.showinfo("Success","Successfully added to database")
            except:
                 messagebox.showerror("ERROR","Can add to database")

        else:
            messagebox.showerror("ERROR","Fields cant be empty")


