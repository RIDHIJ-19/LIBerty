from tkinter import *
from tkinter import ttk
import sqlite3
from typing import List, Any

import addbook, addmember

con = sqlite3.connect('library.db')
cur = con.cursor()


class Main(object):
    def _init_(self, master):
        self.master = master

        def displayStatistics(evt):
            count_books: list[Any] = cur.execute("SELECT count(book_id) FROM books").fetchall()
            count_members = cur.execute("SELECT count(member_id) FROM members").fetchall()
            taken_books = cur.execute("SELECT count(book_status) FROM books WHERE book_status=1").fetchall()
            print(count_books)
            self.lbl_book_count.config(text='Total: ' + str(count_books[0][0]) + 'books in library')
            self.lbl_member_count.config(text='Total members: ' + str(taken_books[0][0]))
            self.lbl_taken_count.config(text='Taken books: ' + str(taken_books[0][0]))
            displayBooks(self)

        def displayBooks(self):
            books = cur.execute("SELECT * FROM books").fetchall()
            count = 0
            self.list_books.delete(0,END)
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

            def doubleClick(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                given_id = value.split('-')[0]
                give_book = GiveBook()

            self.list_books.bind('<<ListboxSelect>>', bookInfo)
            self.tabs.bind('<<NotebookTabChanged>>', displayStatistics)
            #self.tabs.bind('<ButtonRelease-1>', displayBooks)
            self.list_books.bind('Double-Button-1', doubleClick)

        ##frames
        mainFrame = Frame(self.master)
        mainFrame.pack()
        topframe = Frame(mainFrame, width=1350, height=70, bg='cyan', padx=20, relief=SUNKEN, borderwidth=8)
        topframe.pack(side=TOP, fill=X)
        centerframe = Frame(mainFrame, width=1350, relief=RIDGE, bg='#e0f0f0', height=680)
        centerframe.pack(side=TOP)
        centerleftframe = Frame(centerframe, width=900, height=700, borderwidth=5, bg="#e0f0f0", relief=SUNKEN)
        centerleftframe.pack(side=LEFT)
        centerrightframe = Frame(centerframe, width=450, height=700, bg='#e0f0f0', borderwidth=5, relief=SUNKEN)
        centerrightframe.pack()

        # search bar
        search_bar = LabelFrame(centerrightframe, width=440, height=75, text="search box", font=(20), bg="#9bc9ff")
        search_bar.pack(fill=BOTH)
        self.lbl_search = Label(search_bar, text="search:", font="comicsans 12 bold", bg="#9bc9ff", fg="white")
        self.lbl_search.grid(row=0, column=0, padx=20, pady=20)
        self.ent_search = Entry(search_bar, width=30, bd=10)
        self.ent_search.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.btn_search = Button(search_bar, text="search", font="comicsans 12", bg="#fcc324", fg="black",
                                 command=self.searchBooks)
        self.btn_search.grid(row=0, column=4, padx=20, pady=10)

        # list bar

        list_bar = LabelFrame(centerrightframe, width=440, height=175, text="list box", font=(20), bg="#fcc324")
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text="Sort By", font="time 16 bold", fg="#2488ff", bg="#fcc324")
        lbl_list.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text="All Books", var=self.listChoice, value=1, bg="#fcc324")
        rb2 = Radiobutton(list_bar, text="In Library", var=self.listChoice, value=2, bg="#fcc324")
        rb3 = Radiobutton(list_bar, text="Borrowed Books", var=self.listChoice, value=3, bg="#fcc324")
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='List books', bg='#2488ff', fg="black", font="comicsans 12 ",
                          command=self.listBooks)
        btn_list.grid(row=1, column=3, padx=40, pady=10)

        # title and image
        image_bar = Frame(centerrightframe, width=440, height=350)
        image_bar.pack(fill=BOTH)
        self.title_right = Label(image_bar, text="Welcom to our library", font='arial 16 bold')
        self.title_right.grid(row=0)
        self.img_library = PhotoImage(file='')

        #################################################toolbar#######################################################################
        ####add book
        self.btnbook = Button(topframe, text="Add Book", font='comicsans 12 bold', command=self.addbook)
        self.btnbook.pack(side=LEFT, padx=10)
        ##add member
        self.btnmember = Button(topframe, text="add member", font='comicsans 12 bold', command=self.addMember)
        self.btnmember.pack(side=LEFT, padx=10)
        ##givebook
        self.btngive = Button(topframe, text="give book", font="comicsans 12 bold")
        self.btngive.pack(side=LEFT, padx=10)

        #####################################################tabs##############################################
        #####tab1##########
        self.tabs = ttk.Notebook(centerleftframe, width=900, height=660)
        self.tabs.pack()
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text="library management", compound=LEFT)
        self.tabs.add(self.tab2, text="statistics", compound=LEFT)
        ##listbox
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=5, font='times 12 bold')
        self.sb = Scrollbar(self.tab1, orient=VERTICAL)
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N + S + E)
        # listdetails
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='times 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N)
        ########################################################################
        # statistics
        self.lbl_book_count = Label(self.tab2, text="abc", pady=20, font='verdana 14 bold')
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count = Label(self.tab2, text="adb", pady=20, font='verdana 14 bold')
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count = Label(self.tab2, text="sds", pady=20, font='verdana 14 bold')
        self.lbl_taken_count.grid(row=2, sticky=W)

        # functions
        displayBooks(self)
        displayStatistics(self)

    def addbook(self):
        add = addbook.AddBook()

    def addMember(self):
        member = addmember.addMember()

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
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status=?", (0,)).fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in books_in_library:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
        else:
            taken_books = cur.execute("SELECT * FROM books WHERE book_status=?", (1,)).fetchall()
            self.list_books.delete(0, END)

            count = 0
            for book in taken_books:
                self.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
class GiveBook(Toplevel):
    def __init__(self):
        Toplevel._init_(self)
        self.geometry("650x750+550+200")
        self.title("Lend Book")
        self.resizable(False,False)
        global given_id
        self.book_id=int(given_id)

def main():
    root = Tk()
    app = Main(root)
    root.title("library management system")
    root.geometry("1350x750+350+200")

    root.mainloop()


if __name__ == '_main_':
    main()
