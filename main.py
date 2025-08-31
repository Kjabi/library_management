from tkinter import *
from tkinter import ttk
import random
import datetime
from tkinter import messagebox
import pymysql



class library :
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management")
        self.root.geometry("1540x800+0+0")
        root.config(bg="#2C2F33")

        #variables

        self.bookid=StringVar()
        self.booktitle=StringVar()
        self.author=StringVar()
        self.publisher=StringVar()
        self.price=StringVar()
        self.nocopy=StringVar()
        self.memeberid=StringVar()
        self.name=StringVar()
        self.department=StringVar()
        self.phoneno=StringVar()
        self.issueid=StringVar()
        self.issuedate=StringVar()
        self.duedate=StringVar()
        self.returndate=StringVar()
        self.fine=StringVar()

        







#=============Title frame=============
        lbtitle=Label(self.root,bd=10,relief=RIDGE,text="Library Management System",fg="white",bg="#333",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)



#===============data frame=============
        DataFrame = LabelFrame(self.root, bd=8,padx=10,bg="#333", relief=RIDGE, font=("Arial", 12, "bold"),
                                   )
        DataFrame.place(x=0, y=95, width=1670, height=950)


        DataFrameleft=LabelFrame(DataFrame, bd=2,padx=10, relief=RIDGE, font=("Arial", 12, "bold"),
                                   text="Book Details")
        DataFrameleft.place(x=1, y=1, width=810, height=320)

        DataFrameright=LabelFrame(DataFrame, bd=2,padx=10, relief=RIDGE, font=("Arial", 12, "bold"),
                                   text="Members Details")
        DataFrameright.place(x=823, y=1, width=810, height=320)


        DataFramertran=LabelFrame(DataFrame, bd=2,padx=10, relief=RIDGE, font=("Arial", 12, "bold"),
                                   text="Transaction Details")
        DataFramertran.place(y=320, width=1635, height=250)


        DataFramerfunc=LabelFrame(DataFrame, bd=2,padx=10, relief=RIDGE, font=("Arial", 12, "bold"),
                                   )
        DataFramerfunc.place(y=575, width=1635, height=100)


        DataFramerdetil=LabelFrame(DataFrame, bd=2,padx=10, relief=RIDGE, font=("Arial", 12, "bold"),
                                   text="Log")
        DataFramerdetil.place(y=680, width=1635, height=250)




#=========================text fields(left(book details))============================
       # ===================== BOOK DETAILS (LEFT) =====================
        bookid = Label(DataFrameleft, font=("Arial", 20, "bold"), text="Book ID:")
        bookid.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        txtbookid = Entry(DataFrameleft, font=("Arial", 13, "bold"), textvariable=self.bookid, width=35)
        txtbookid.grid(row=0, column=1, padx=10, pady=5)

        booktitle = Label(DataFrameleft, font=("Arial", 20, "bold"), text="Title:")
        booktitle.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        txtbooktitle = Entry(DataFrameleft, font=("Arial", 13, "bold"), textvariable=self.booktitle, width=35)
        txtbooktitle.grid(row=1, column=1, padx=10, pady=5)

        author = Label(DataFrameleft, font=("Arial", 20, "bold"), text="Author:")
        author.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        txtauthor = Entry(DataFrameleft, font=("Arial", 13, "bold"), textvariable=self.author, width=35)
        txtauthor.grid(row=2, column=1, padx=10, pady=5)

        publisher = Label(DataFrameleft, font=("Arial", 20, "bold"), text="Publisher:")
        publisher.grid(row=3, column=0, sticky=W, padx=10, pady=5)
        txtpublisher = Entry(DataFrameleft, font=("Arial", 13, "bold"), textvariable=self.publisher, width=35)
        txtpublisher.grid(row=3, column=1, padx=10, pady=5)

        price = Label(DataFrameleft, font=("Arial", 20, "bold"), text="Price:")
        price.grid(row=4, column=0, sticky=W, padx=10, pady=5)
        txtprice = Entry(DataFrameleft, font=("Arial", 13, "bold"), textvariable=self.price, width=35)
        txtprice.grid(row=4, column=1, padx=10, pady=5)

        nocopy = Label(DataFrameleft, font=("Arial", 20, "bold"), text="No Of Copies:")
        nocopy.grid(row=5, column=0, sticky=W, padx=10, pady=5)
        txtnocopy = Entry(DataFrameleft, font=("Arial", 13, "bold"), textvariable=self.nocopy, width=35)
        txtnocopy.grid(row=5, column=1, padx=10, pady=5)

        # ===================== MEMBER DETAILS (RIGHT) =====================
        membertitle = Label(DataFrameright, fg="white", bg="#333", font=("Times New Roman", 30, "bold"), text="Students Details")
        membertitle.grid(row=0, column=0, columnspan=2, pady=5)

        memberid = Label(DataFrameright, font=("Arial", 20, "bold"), text="Student ID:")
        memberid.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        txtmemberid = Entry(DataFrameright, font=("Arial", 13, "bold"), textvariable=self.memeberid, width=35)
        txtmemberid.grid(row=1, column=1, padx=10, pady=5)

        name = Label(DataFrameright, font=("Arial", 20, "bold"), text="Name:")
        name.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        txtname = Entry(DataFrameright, font=("Arial", 13, "bold"), textvariable=self.name, width=35)
        txtname.grid(row=2, column=1, padx=10, pady=5)

        dept = Label(DataFrameright, font=("Arial", 20, "bold"), text="Department:")
        dept.grid(row=3, column=0, sticky=W, padx=10, pady=5)
        txtdept = Entry(DataFrameright, font=("Arial", 13, "bold"), textvariable=self.department, width=35)
        txtdept.grid(row=3, column=1, padx=10, pady=5)

        phoneno = Label(DataFrameright, font=("Arial", 20, "bold"), text="Phone No:")
        phoneno.grid(row=4, column=0, sticky=W, padx=10, pady=5)
        txtphoneno = Entry(DataFrameright, font=("Arial", 13, "bold"), textvariable=self.phoneno, width=35)
        txtphoneno.grid(row=4, column=1, padx=10, pady=5)

        # ===================== TRANSACTION DETAILS =====================
        trandetitle = Label(DataFramertran, fg="white", bg="#333", font=("Times New Roman", 30, "bold"), text="Transaction Details")
        trandetitle.grid(row=0, column=0, columnspan=4, pady=10)

        issueid = Label(DataFramertran, font=("Arial", 20, "bold"), text="Issue ID:")
        issueid.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        txtissueid = Entry(DataFramertran, font=("Arial", 13, "bold"), textvariable=self.issueid, width=35)
        txtissueid.grid(row=1, column=1, padx=10, pady=5)

        issuedate = Label(DataFramertran, font=("Arial", 20, "bold"), text="Issue Date:")
        issuedate.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        txtissuedate = Entry(DataFramertran, font=("Arial", 13, "bold"), textvariable=self.issuedate, width=35)
        txtissuedate.grid(row=2, column=1, padx=10, pady=5)

        duedate = Label(DataFramertran, font=("Arial", 20, "bold"), text="Due Date:")
        duedate.grid(row=3, column=0, sticky=W, padx=10, pady=5)
        txtduedate = Entry(DataFramertran, font=("Arial", 13, "bold"), textvariable=self.duedate, width=35)
        txtduedate.grid(row=3, column=1, padx=10, pady=5)

        returndate = Label(DataFramertran, font=("Arial", 20, "bold"), text="Return Date:")
        returndate.grid(row=1, column=2, sticky=W, padx=50, pady=5)
        txtreturndate = Entry(DataFramertran, font=("Arial", 13, "bold"), textvariable=self.returndate, width=35)
        txtreturndate.grid(row=1, column=3, padx=10, pady=5)

        fine = Label(DataFramertran, font=("Arial", 20, "bold"), text="Fine:")
        fine.grid(row=2, column=2, sticky=W, padx=50, pady=5)
        txtfine = Entry(DataFramertran, font=("Arial", 13, "bold"), textvariable=self.fine, width=35)
        txtfine.grid(row=2, column=3, padx=10, pady=5)



#====================functiom button===========================
        
        btnaddbook = Button(DataFramerfunc, text="Add Book",command=self.addbook, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btnaddbook.grid(row=1, column=0, padx=30)

        

        btnupdate = Button(DataFramerfunc, text="Update",command=self.updatebook, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btnupdate.grid(row=1, column=2, padx=30)

        btndeleted = Button(DataFramerfunc, text="Delete Book",command= self.deletebook, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btndeleted.grid(row=1, column=4, padx=30)

        btnissuebook = Button(DataFramerfunc, text="Issue book",command=self.issue_book, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btnissuebook.grid(row=1, column=6, padx=30)

        btnreturnbook = Button(DataFramerfunc, text="Returnbook",command=self.return_book, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btnreturnbook.grid(row=1, column=8, padx=30)

        btnclear = Button(DataFramerfunc, text="clear",command=self.reset_librarydata, bg="blue", fg="white",
                         font=("Arial", 13, "bold"), width=16, height=2)
        btnclear.grid(row=1, column=10, padx=30)


#==================scroll bar===================

        # ===================== TREEVIEW (LOG / BOOK RECORDS) =====================
        scroll_x = ttk.Scrollbar(DataFramerdetil, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DataFramerdetil, orient=VERTICAL)

        self.library = ttk.Treeview(
        DataFramerdetil,
        columns=(
                "BookID",
                "Title",
                "Author",
                "Publisher",
                "Price",
                "NoOfCopies",
                "StudentID",
                "StudentName",
                "Department",
                "PhoneNo",
                "IssueID",
                "IssueDate",
                "DueDate",
                "ReturnDate",
                "Fine",
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.library.xview)
        scroll_y.config(command=self.library.yview)

        # ===================== HEADINGS =====================
        self.library.heading("BookID", text="Book ID")
        self.library.heading("Title", text="Title")
        self.library.heading("Author", text="Author")
        self.library.heading("Publisher", text="Publisher")
        self.library.heading("Price", text="Price")
        self.library.heading("NoOfCopies", text="No Of Copies")
        self.library.heading("StudentID", text="Student ID")
        self.library.heading("StudentName", text="Student Name")
        self.library.heading("Department", text="Department")
        self.library.heading("PhoneNo", text="Phone No")
        self.library.heading("IssueID", text="Issue ID")
        self.library.heading("IssueDate", text="Issue Date")
        self.library.heading("DueDate", text="Due Date")
        self.library.heading("ReturnDate", text="Return Date")
        self.library.heading("Fine", text="Fine")

        self.library["show"] = "headings"

        # ===================== COLUMN WIDTHS =====================
        self.library.column("BookID", width=100)
        self.library.column("Title", width=150)
        self.library.column("Author", width=140)
        self.library.column("Publisher", width=140)
        self.library.column("Price", width=80)
        self.library.column("NoOfCopies", width=120)
        self.library.column("StudentID", width=120)
        self.library.column("StudentName", width=150)
        self.library.column("Department", width=130)
        self.library.column("PhoneNo", width=130)
        self.library.column("IssueID", width=100)
        self.library.column("IssueDate", width=120)
        self.library.column("DueDate", width=120)
        self.library.column("ReturnDate", width=120)
        self.library.column("Fine", width=80)

        self.library.pack(fill=BOTH, expand=1)
        self.library.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetchdata()

#=============functionality===========================

    def addbook(self):
        if self.bookid.get()=="" or self.booktitle.get()=="":
                messagebox.showerror("Error","All fields are required!")
                return
        
        try:
                conn = pymysql.connect(
                host="localhost",          
                user="root",         # New user
                password="abisheek",     # New password
                database="library_db"
                
                )
                cursor = conn.cursor()
                print("Connected")

                cursor.execute("""
                INSERT INTO library_management
                (title, author, publisher, price, no_of_copies,
                student_id, student_name, department, phone_no,
                issue_id, issue_date, due_date, return_date, fine)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                self.booktitle.get(),
                self.author.get(),
                self.publisher.get(),
                self.price.get(),
                self.nocopy.get(),
                self.memeberid.get(),
                self.name.get(),
                self.department.get(),
                self.phoneno.get(),
                self.issueid.get(),
                self.issuedate.get(),
                self.duedate.get(),
                self.returndate.get(),
                self.fine.get()
                ))

                conn.commit()
                messagebox.showinfo("Success", "Book added successfully!")
                conn.close()

        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")
    

    def updatebook(self):
        if self.booktitle.get() == "" or self.author.get() == "":
                messagebox.showerror("Error", "All Fields Are Required")
                return

        try:
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="library_db"
                )
                cursor = conn.cursor()
                print("Connected")

                # Convert empty date fields to None
                issue_date = self.issuedate.get() or None
                due_date = self.duedate.get() or None
                return_date = self.returndate.get() or None

                cursor.execute("""
                UPDATE library_management
                SET title = %s,
                        author = %s,
                        publisher = %s,
                        price = %s,
                        no_of_copies = %s,
                        student_id = %s,
                        student_name = %s,
                        department = %s,
                        phone_no = %s,
                        issue_id = %s,
                        issue_date = %s,
                        due_date = %s,
                        return_date = %s,
                        fine = %s
                WHERE book_id = %s
                """, (
                self.booktitle.get(),
                self.author.get(),
                self.publisher.get(),
                self.price.get(),
                self.nocopy.get(),
                self.memeberid.get(),
                self.name.get(),
                self.department.get(),
                self.phoneno.get(),
                self.issueid.get(),
                issue_date,
                due_date,
                return_date,
                self.fine.get(),
                self.bookid.get()
                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Book details updated successfully!")

        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")

                
    def fetchdata(self):
          conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="library_db"
                )
          cursor = conn.cursor()
          cursor.execute("SELECT * FROM library_management")
          rows=cursor.fetchall()
          if len(rows) != 0:
                self.library.delete(*self.library.get_children())
                for row in rows:
                        self.library.insert("", END, values=row)
                conn.commit()
          conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library.focus()  # Get selected row's ID
        content = self.library.item(cursor_row)  # Get data of that row
        row = content['values']  # Extract values list

        if row:  # Check if row is not empty
                self.bookid.set(row[0])
                self.booktitle.set(row[1])
                self.author.set(row[2])
                self.publisher.set(row[3])
                self.price.set(row[4])
                self.nocopy.set(row[5])
                self.memeberid.set(row[6])
                self.name.set(row[7])
                self.department.set(row[8])
                self.phoneno.set(row[9])
                self.issueid.set(row[10])
                self.issuedate.set(row[11])
                self.duedate.set(row[12])
                self.returndate.set(row[13])
                self.fine.set(row[14])


    def deletebook(self):
    # Check if Book ID is provided
        if self.bookid.get() == "":
                messagebox.showerror("Error", "Book ID is required to delete a record!")
                return

        try:
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="library_db"
                )
                cursor = conn.cursor()

                # Execute DELETE query
                cursor.execute("DELETE FROM library_management WHERE book_id=%s", (self.bookid.get(),))

                if cursor.rowcount == 0:
                        messagebox.showwarning("Warning", "No record found with this Book ID!")
                else:
                        conn.commit()
                        messagebox.showinfo("Success", "Book Deleted Successfully!")

                conn.close()

        except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")

                
    def reset_librarydata(self):
        try:
                # Clear all entry field variables
                self.bookid.set("")
                self.booktitle.set("")
                self.author.set("")
                self.publisher.set("")
                self.price.set("")
                self.nocopy.set("")
                self.memeberid.set("")
                self.name.set("")
                self.department.set("")
                self.phoneno.set("")
                self.issueid.set("")
                self.issuedate.set("")
                self.duedate.set("")
                self.returndate.set("")
                self.fine.set("")

                messagebox.showinfo("Reset", "All fields have been cleared!")

        except Exception as e:
                messagebox.showerror("Error", f"Reset Error: {str(e)}")


    def issue_book(self):
        try:
                # Get all values from Tkinter form variables
                book_id = self.book_id.get()
                student_id = self.student_id.get()
                issue_date = self.issue_date.get()
                due_date = self.due_date.get()
                return_date = self.return_date.get()  # Can be empty at issue time
                fine = self.fine.get()

                # Basic validation
                if book_id == "" or student_id == "" or issue_date == "" or due_date == "":
                        messagebox.showerror("Error", "Book ID, Student ID, Issue Date, and Due Date are required!")
                        return

                if return_date.strip() == "":
                        return_date = None

             
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="library_db"
                )
                cursor = conn.cursor()

                # SQL query with proper date handling
                sql = """
                INSERT INTO issue_book (book_id, student_id, issue_date, due_date, return_date, fine)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (book_id, student_id, issue_date, due_date, return_date, fine))

                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Book issued successfully!")
                self.reset_librarydata()  # Clear form after issuing

        except Exception as e:
                messagebox.showerror("Database Error", str(e))




    def issue_book(self):
        try:
                # Get field values
                title = self.title.get()
                author = self.author.get()
                publisher = self.publisher.get()
                price = self.price.get()
                no_of_copies = self.no_of_copies.get()
                student_id = self.student_id.get()
                student_name = self.student_name.get()
                department = self.department.get()
                phone_no = self.phone_no.get()
                issue_id = self.issue_id.get()
                issue_date = self.issue_date.get()
                due_date = self.due_date.get()

                # Basic validation
                if not title or not student_id or not student_name or not issue_date or not due_date:
                        messagebox.showerror("Error", "Please fill all required fields!")
                        return

                # Connect to MySQL
                conn = pymysql.connect(
                host="localhost",
                user="root",
                password="abisheek",
                database="library_db"
                )
                cursor = conn.cursor()

                # Insert book issue record
                cursor.execute("""
                INSERT INTO library_management
                (title, author, publisher, price, no_of_copies, student_id, student_name, department, phone_no, issue_id, issue_date, due_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                title, author, publisher, price, no_of_copies, student_id,
                student_name, department, phone_no, issue_id, issue_date, due_date
                ))

                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Book issued successfully!")

                # Optional: Clear fields after issuing
                self.reset_issue_book()

        except Exception as e:
                messagebox.showerror("Error", f"Error issuing book: {str(e)}")







    def return_book(self):
        if self.bookid.get() == "" or self.memberid.get() == "":
                messagebox.showerror("Error", "Book ID and Member ID are required!")
                return

        try:
                conn = pymysql.connect(
                host="localhost",
                user="pythonuser",
                password="yourpassword",
                database="library"
                )
                cursor = conn.cursor()

                # Check if the book was issued to this member
                cursor.execute("""
                SELECT * FROM issued_books 
                WHERE bookid=%s AND memberid=%s AND return_date IS NULL
                """, (self.bookid.get(), self.memberid.get()))
                record = cursor.fetchone()

                if record is None:
                        messagebox.showerror("Error", "No active issue found for this book and member!")
                        conn.close()
                        return

                # Update the return date
                from datetime import date
                today = date.today()
                cursor.execute("""
                UPDATE issued_books
                SET return_date=%s
                WHERE bookid=%s AND memberid=%s AND return_date IS NULL
                """, (today, self.bookid.get(), self.memberid.get()))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Book ID {self.bookid.get()} returned successfully!")

        except Exception as e:
                messagebox.showerror("Database Error", f"{str(e)}")





















if __name__=="__main__":
        root=Tk()
        obj=library(root)
        root.mainloop()