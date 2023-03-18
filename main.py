from tkinter import *
from tkinter import ttk
import sqlite3
import addbook , addmember,delmember,login
import record,returnBook,reserveb

con=sqlite3.connect('library.db')
cur=con.cursor()

class Main(object):
    def __init__(self,master):
        self.master= master


        def displayBooks(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0
            for book in books:
                print(book)
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1

            def bookInfo(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE book_id=?", (id,))
                book_info = book.fetchall()
                print(book_info)
                self.list_details.delete(0, 'end')
                self.list_details.insert(0, "Book Name: " + book_info[0][1])
                self.list_details.insert(1, "Author: " + book_info[0][2])
                self.list_details.insert(2, "Page: " + book_info[0][3])
                self.list_details.insert(3, "Language: " + book_info[0][4])
                if book_info[0][5] == 0:
                    self.list_details.insert(4, "Status : Available")
                else:
                    self.list_details.insert(4, 4, "Status : Not Available")


            self.list_books.bind('<<ListboxSelect>>',bookInfo)
            self.tabs.bind('<ButtonRelease-1>', displayBooks)

        ##frames
        mainFrame=Frame(self.master)
        mainFrame.pack()
        topframe=Frame(mainFrame,width=1350,height=70,bg='#708d8d',padx=20,relief=SUNKEN,borderwidth=8)##light cyan
        topframe.pack(side=TOP,fill=X)
        centerframe=Frame(mainFrame,width=1350,relief=RIDGE,bg='#d4d4d4',height=680)##grey box
        centerframe.pack(side=TOP)
        centerleftframe=Frame(centerframe,width=900,height=700,borderwidth=5,bg="#e0f0f0",relief=SUNKEN)
        centerleftframe.pack(side=LEFT)
        centerrightframe=Frame(centerframe,width=450,height=700,bg='black',borderwidth=5,relief=SUNKEN)
        centerrightframe.pack()

        #search bar
        search_bar=LabelFrame(centerrightframe,width=440,height=75,text="Search Box",font=(20),bg="#c4b48c",fg="black")
        search_bar.pack(fill=BOTH)
        self.lbl_search=Label(search_bar,text="Search:",font="comicsans 12 bold",bg="#8b8680",fg="white")##search pehla vala
        self.lbl_search.grid(row=0,column=0,padx=20,pady=20)
        self.ent_search=Entry(search_bar,width=30,bd=10)
        self.ent_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        ##search dusra vala
        self.btn_search=Button(search_bar,text="Search",font="comicsans 13",bg="black",fg="white",command=self.searchBooks)
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)





        #list bar

        list_bar=LabelFrame(centerrightframe,width=440,height=175,text="List Box",fg="black",font=(20),bg="#526a5d")
        list_bar.pack(fill=BOTH)
        lbl_list=Label(list_bar,text="Sort By",font="time 16 bold", bg="#8b8680",fg="white")
        lbl_list.grid(row=0,column=2)
        self.listChoice=IntVar()
        rb1 = Radiobutton(list_bar,text="All Books",var=self.listChoice,value=1,bg="black",fg="white")
        rb2 = Radiobutton(list_bar, text="In Library", var=self.listChoice, value=2, bg="black",fg="white")
        rb3 = Radiobutton(list_bar, text="Borrowed Books", var=self.listChoice, value=3, bg="black",fg="white")
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        btn_list=Button(list_bar,text='List books',bg='#c4b48c',fg="black",font="comicsans 12 ",command=self.listBooks)
        btn_list.grid(row=1,column=3,padx=40,pady=10)


        ############# fine
        search_bar = LabelFrame(centerrightframe, width=440, height=275, text="Fine Management", font=(20), bg="#c4b48c",
                                fg="black")
        search_bar.pack(fill=BOTH)



        ##search dusra vala
        self.btn_search2 = Button(search_bar, text="Manage", font="comicsans 13", bg="black", fg="white",
                                 command=self.record)
        self.btn_search2.grid(row=50, column=2, padx=20, pady=10)

        # list bar2
        ##########recommendation box

        list_bar = LabelFrame(centerrightframe, width=440, height=175, text="Recommendation Box", fg="black", font=(20),
                              bg="#526a5d")
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text="Genre", font="time 16 bold", bg="#8b8680", fg="white")
        lbl_list.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text="Thriller", var=self.listChoice, value=1, bg="black", fg="white")
        rb2 = Radiobutton(list_bar, text="Comedy", var=self.listChoice, value=2, bg="black", fg="white")
        rb3 = Radiobutton(list_bar, text="Horror", var=self.listChoice, value=3, bg="black", fg="white")
        rb4 = Radiobutton(list_bar, text="Romance", var=self.listChoice, value=4, bg="black", fg="white")
        rb5 = Radiobutton(list_bar, text="friction", var=self.listChoice, value=5, bg="black", fg="white")
        rb6 = Radiobutton(list_bar, text="Young Adult", var=self.listChoice, value=6, bg="black", fg="white")
        rb7 = Radiobutton(list_bar, text="Fantasy", var=self.listChoice, value=7, bg="black", fg="white")


        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        rb4.grid(row=1, column=3)
        rb5.grid(row=1, column=4)
        rb6.grid(row=2, column=0)
        rb7.grid(row=2, column=1)




        #title and image
        image_bar=Frame(centerrightframe,width=440,height=450)
        image_bar.pack(fill=BOTH)
        self.title_right=Label(image_bar,text="Welcome To Our library",font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library=PhotoImage(file="lib.png")


#################################################toolbar#######################################################################
      ####add book
        self.btnbook=Button(topframe,text="Add Book",font='comicsans 12 bold',command=self.addbook)
        self.btnbook.pack(side=LEFT,padx=10)
        ##add member
        self.btnmember=Button(topframe,text="Add Member",font='comicsans 12 bold',command=self.addMember)
        self.btnmember.pack(side=LEFT,padx=10)
        ##delete member
        self.btndel = Button(topframe, text="Delete Member", font="comicsans 12 bold",command=self.delmember)
        self.btndel.pack(side=LEFT, padx=10)
        ##givebook
        self.btngive=Button(topframe,text="Issue Book ",font="comicsans 12 bold")
        self.btngive.pack(side=LEFT,padx=10)
        ##return
        self.btngive = Button(topframe, text="Return Book ", font="comicsans 12 bold",command=self.returnb)
        self.btngive.pack(side=LEFT, padx=10)
        ##reserve
        self.btngive = Button(topframe, text="Reserve Book ", font="comicsans 12 bold",command=self.reserve)
        self.btngive.pack(side=LEFT, padx=10)

        #LOGIN
        self.btngive = Button(topframe, text="Login ", font="comicsans 12 bold",command=self.login)
        self.btngive.pack(side=RIGHT, padx=10)



        #####################################################tabs##############################################
               #####tab1##########
        self.tabs=ttk.Notebook(centerleftframe,width=900,height=660)
        self.tabs.pack()
        self.tab1=ttk.Frame(self.tabs)
        self.tab2=ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text="Library Management",compound=LEFT )
        self.tabs.add(self.tab2,text="Statistics",compound=LEFT)
        ##listbox
        self.list_books=Listbox(self.tab1,width=40,height=30,bd=5,font='times 12 bold')
        self.sb=Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        #listdetails
        self.list_details=Listbox(self.tab1,width=80,height=30,bd=5,font='times 12 bold')
        self.list_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)
        ########################################################################
        # statistics
        self.lbl_book_count = Label(self.tab2, text="Total: 14", pady=20, font='comicsans 20 italic')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="Borrowed : 2", pady=20, font='comicsans  20 italic')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="Members : 3 ", pady=20, font='comicsans  20 italic')
        self.lbl_taken_count.grid(row=2, sticky=W)


        #functions
        displayBooks(self)



    def addbook(self):
        add=addbook.AddBook()

    def addMember(self):
        member=addmember.addMember()

    def delmember(self):
        member1 = delmember.delmember()
    def login(self):
        log = login.login()

    def record(self):
        fine = record.record()
    def returnb(self):
        ret=returnBook.returnBook()
    def reserve(self):
        reserve = reserveb.reserve()


    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%' + value + '%',)).fetchall()
        print(search)
        self.list_books.delete(0, END)
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0]) + "-" + book[1])
            count += 1

    def listBooks(self, books_library=None):
        value = self.listChoice.get()
        if value == 1:
            allBooks = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0, END)
            count = 0
            for book in allBooks:
                self.list_books.insert(count, str(book[0]) + "-"+book[1])
                count += 1
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status=?", (0,)).fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in books_library:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
        else:
            taken_books = cur.execute("SELECT * FROM books WHERE book_status=?", (1,)).fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in taken_books:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1


def main():
    root=Tk()
    app=Main(root)
    root.title("library management system")
    root.geometry("1350x800+350+200")
 
    root.mainloop()
if __name__ == '__main__':
    main()
