from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from datetime import date


class library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x950")
        self.root.config(bg="#2C2F33")

        # ================= VARIABLES =================

        self.bookid = StringVar()
        self.booktitle = StringVar()
        self.author = StringVar()
        self.publisher = StringVar()
        self.price = StringVar()
        self.nocopy = StringVar()

        self.memeberid = StringVar()
        self.name = StringVar()
        self.department = StringVar()
        self.phoneno = StringVar()

        self.issueid = StringVar()
        self.issuedate = StringVar()
        self.duedate = StringVar()
        self.returndate = StringVar()
        self.fine = StringVar()

        # ================= TITLE =================

        lbtitle = Label(
            self.root,
            bd=10,
            relief=RIDGE,
            text="Library Management System",
            fg="white",
            bg="#333333",
            font=("Times New Roman", 35, "bold")
        )
        lbtitle.pack(side=TOP, fill=X)

        # ================= MAIN DATA FRAME =================

        DataFrame = LabelFrame(
            self.root,
            bd=8,
            padx=10,
            bg="#333333",
            relief=RIDGE
        )
        DataFrame.place(x=0, y=85, width=1490, height=850)

        # ================= BOOK DETAILS =================

        DataFrameleft = LabelFrame(
            DataFrame,
            bd=2,
            padx=10,
            relief=RIDGE,
            text="Book Details",
            font=("Arial", 12, "bold")
        )
        DataFrameleft.place(x=1, y=1, width=720, height=300)

        # ================= MEMBER DETAILS =================

        DataFrameright = LabelFrame(
            DataFrame,
            bd=2,
            padx=10,
            relief=RIDGE,
            text="Member Details",
            font=("Arial", 12, "bold")
        )
        DataFrameright.place(x=730, y=1, width=730, height=300)

        # ================= TRANSACTION DETAILS =================

        DataFramertran = LabelFrame(
            DataFrame,
            bd=2,
            padx=10,
            relief=RIDGE,
            text="Transaction Details",
            font=("Arial", 12, "bold")
        )
        DataFramertran.place(x=1, y=305, width=1459, height=220)

        # ================= BUTTON FRAME =================

        DataFramerfunc = LabelFrame(
            DataFrame,
            bd=2,
            padx=10,
            relief=RIDGE
        )
        DataFramerfunc.place(x=1, y=530, width=1459, height=90)

        # ================= LOG FRAME =================

        DataFramerdetil = LabelFrame(
            DataFrame,
            bd=2,
            padx=10,
            relief=RIDGE,
            text="Library Records",
            font=("Arial", 12, "bold")
        )
        DataFramerdetil.place(x=1, y=625, width=1459, height=210)

        # =========================================================
        # BOOK DETAILS
        # =========================================================

        Label(
            DataFrameleft,
            font=("Arial", 15, "bold"),
            text="Book ID:"
        ).grid(row=0, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameleft,
            font=("Arial", 12, "bold"),
            textvariable=self.bookid,
            width=30
        ).grid(row=0, column=1, padx=10, pady=5)

        Label(
            DataFrameleft,
            font=("Arial", 15, "bold"),
            text="Title:"
        ).grid(row=1, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameleft,
            font=("Arial", 12, "bold"),
            textvariable=self.booktitle,
            width=30
        ).grid(row=1, column=1, padx=10, pady=5)

        Label(
            DataFrameleft,
            font=("Arial", 15, "bold"),
            text="Author:"
        ).grid(row=2, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameleft,
            font=("Arial", 12, "bold"),
            textvariable=self.author,
            width=30
        ).grid(row=2, column=1, padx=10, pady=5)

        Label(
            DataFrameleft,
            font=("Arial", 15, "bold"),
            text="Publisher:"
        ).grid(row=3, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameleft,
            font=("Arial", 12, "bold"),
            textvariable=self.publisher,
            width=30
        ).grid(row=3, column=1, padx=10, pady=5)

        Label(
            DataFrameleft,
            font=("Arial", 15, "bold"),
            text="Price:"
        ).grid(row=4, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameleft,
            font=("Arial", 12, "bold"),
            textvariable=self.price,
            width=30
        ).grid(row=4, column=1, padx=10, pady=5)

        Label(
            DataFrameleft,
            font=("Arial", 15, "bold"),
            text="No Of Copies:"
        ).grid(row=5, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameleft,
            font=("Arial", 12, "bold"),
            textvariable=self.nocopy,
            width=30
        ).grid(row=5, column=1, padx=10, pady=5)

        # =========================================================
        # MEMBER DETAILS
        # =========================================================

        Label(
            DataFrameright,
            fg="white",
            bg="#333333",
            font=("Times New Roman", 23, "bold"),
            text="Student Details"
        ).grid(row=0, column=0, columnspan=2, pady=5)

        Label(
            DataFrameright,
            font=("Arial", 15, "bold"),
            text="Student ID:"
        ).grid(row=1, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameright,
            font=("Arial", 12, "bold"),
            textvariable=self.memeberid,
            width=30
        ).grid(row=1, column=1, padx=10, pady=5)

        Label(
            DataFrameright,
            font=("Arial", 15, "bold"),
            text="Name:"
        ).grid(row=2, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameright,
            font=("Arial", 12, "bold"),
            textvariable=self.name,
            width=30
        ).grid(row=2, column=1, padx=10, pady=5)

        Label(
            DataFrameright,
            font=("Arial", 15, "bold"),
            text="Department:"
        ).grid(row=3, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameright,
            font=("Arial", 12, "bold"),
            textvariable=self.department,
            width=30
        ).grid(row=3, column=1, padx=10, pady=5)

        Label(
            DataFrameright,
            font=("Arial", 15, "bold"),
            text="Phone No:"
        ).grid(row=4, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFrameright,
            font=("Arial", 12, "bold"),
            textvariable=self.phoneno,
            width=30
        ).grid(row=4, column=1, padx=10, pady=5)

        # =========================================================
        # TRANSACTION DETAILS
        # =========================================================

        Label(
            DataFramertran,
            fg="white",
            bg="#333333",
            font=("Times New Roman", 23, "bold"),
            text="Transaction Details"
        ).grid(row=0, column=0, columnspan=4, pady=5)

        Label(
            DataFramertran,
            font=("Arial", 15, "bold"),
            text="Issue ID:"
        ).grid(row=1, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFramertran,
            font=("Arial", 12, "bold"),
            textvariable=self.issueid,
            width=28
        ).grid(row=1, column=1, padx=10, pady=5)

        Label(
            DataFramertran,
            font=("Arial", 15, "bold"),
            text="Issue Date:"
        ).grid(row=2, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFramertran,
            font=("Arial", 12, "bold"),
            textvariable=self.issuedate,
            width=28
        ).grid(row=2, column=1, padx=10, pady=5)

        Label(
            DataFramertran,
            font=("Arial", 15, "bold"),
            text="Due Date:"
        ).grid(row=3, column=0, sticky=W, padx=10, pady=5)

        Entry(
            DataFramertran,
            font=("Arial", 12, "bold"),
            textvariable=self.duedate,
            width=28
        ).grid(row=3, column=1, padx=10, pady=5)

        Label(
            DataFramertran,
            font=("Arial", 15, "bold"),
            text="Return Date:"
        ).grid(row=1, column=2, sticky=W, padx=50, pady=5)

        Entry(
            DataFramertran,
            font=("Arial", 12, "bold"),
            textvariable=self.returndate,
            width=28
        ).grid(row=1, column=3, padx=10, pady=5)

        Label(
            DataFramertran,
            font=("Arial", 15, "bold"),
            text="Fine:"
        ).grid(row=2, column=2, sticky=W, padx=50, pady=5)

        Entry(
            DataFramertran,
            font=("Arial", 12, "bold"),
            textvariable=self.fine,
            width=28
        ).grid(row=2, column=3, padx=10, pady=5)

        # =========================================================
        # BUTTONS
        # =========================================================

        Button(
            DataFramerfunc,
            text="Add Book",
            command=self.addbook,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2
        ).grid(row=1, column=0, padx=15, pady=10)

        Button(
            DataFramerfunc,
            text="Update",
            command=self.updatebook,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2
        ).grid(row=1, column=1, padx=15, pady=10)

        Button(
            DataFramerfunc,
            text="Delete Book",
            command=self.deletebook,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2
        ).grid(row=1, column=2, padx=15, pady=10)

        Button(
            DataFramerfunc,
            text="Issue Book",
            command=self.issue_book,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2
        ).grid(row=1, column=3, padx=15, pady=10)

        Button(
            DataFramerfunc,
            text="Return Book",
            command=self.return_book,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2
        ).grid(row=1, column=4, padx=15, pady=10)

        Button(
            DataFramerfunc,
            text="Clear",
            command=self.reset_librarydata,
            bg="blue",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2
        ).grid(row=1, column=5, padx=15, pady=10)

        # =========================================================
        # TREEVIEW
        # =========================================================

        scroll_x = ttk.Scrollbar(
            DataFramerdetil,
            orient=HORIZONTAL
        )

        scroll_y = ttk.Scrollbar(
            DataFramerdetil,
            orient=VERTICAL
        )

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
                "Fine"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(
            side=BOTTOM,
            fill=X
        )

        scroll_y.pack(
            side=RIGHT,
            fill=Y
        )

        scroll_x.config(
            command=self.library.xview
        )

        scroll_y.config(
            command=self.library.yview
        )

        self.library["show"] = "headings"

        headings = {
            "BookID": "Book ID",
            "Title": "Title",
            "Author": "Author",
            "Publisher": "Publisher",
            "Price": "Price",
            "NoOfCopies": "No Of Copies",
            "StudentID": "Student ID",
            "StudentName": "Student Name",
            "Department": "Department",
            "PhoneNo": "Phone No",
            "IssueID": "Issue ID",
            "IssueDate": "Issue Date",
            "DueDate": "Due Date",
            "ReturnDate": "Return Date",
            "Fine": "Fine"
        }

        for column, heading in headings.items():
            self.library.heading(
                column,
                text=heading
            )

        widths = {
            "BookID": 90,
            "Title": 140,
            "Author": 120,
            "Publisher": 120,
            "Price": 80,
            "NoOfCopies": 100,
            "StudentID": 100,
            "StudentName": 130,
            "Department": 110,
            "PhoneNo": 110,
            "IssueID": 90,
            "IssueDate": 100,
            "DueDate": 100,
            "ReturnDate": 100,
            "Fine": 70
        }

        for column, width in widths.items():
            self.library.column(
                column,
                width=width
            )

        self.library.pack(
            fill=BOTH,
            expand=1
        )

        self.library.bind(
            "<ButtonRelease-1>",
            self.get_cursor
        )

        # Load records
        self.fetchdata()

    # =========================================================
    # DATABASE CONNECTION
    # =========================================================

    def connect_database(self):
        return pymysql.connect(
            host="localhost",
            user="root",
            password="abisheek",
            database="library_db"
        )

    # =========================================================
    # ADD BOOK
    # =========================================================

    def addbook(self):

        if (
            self.bookid.get() == "" or
            self.booktitle.get() == "" or
            self.author.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "Book ID, Title and Author are required!"
            )
            return

        try:

            conn = self.connect_database()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT book_id FROM library_management WHERE book_id=%s",
                (self.bookid.get(),)
            )

            existing = cursor.fetchone()

            if existing:
                messagebox.showerror(
                    "Error",
                    "Book ID already exists!"
                )
                conn.close()
                return

            cursor.execute(
                """
                INSERT INTO library_management
                (
                    book_id,
                    title,
                    author,
                    publisher,
                    price,
                    no_of_copies,
                    student_id,
                    student_name,
                    department,
                    phone_no,
                    issue_id,
                    issue_date,
                    due_date,
                    return_date,
                    fine
                )
                VALUES
                (
                    %s,%s,%s,%s,%s,
                    %s,%s,%s,%s,%s,
                    %s,%s,%s,%s,%s
                )
                """,
                (
                    self.bookid.get(),
                    self.booktitle.get(),
                    self.author.get(),
                    self.publisher.get(),
                    self.price.get(),
                    self.nocopy.get(),
                    self.memeberid.get() or None,
                    self.name.get() or None,
                    self.department.get() or None,
                    self.phoneno.get() or None,
                    self.issueid.get() or None,
                    self.issuedate.get() or None,
                    self.duedate.get() or None,
                    self.returndate.get() or None,
                    self.fine.get() or 0
                )
            )

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Book added successfully!"
            )

            self.fetchdata()
            self.reset_librarydata(show_message=False)

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # UPDATE BOOK
    # =========================================================

    def updatebook(self):

        if self.bookid.get() == "":
            messagebox.showerror(
                "Error",
                "Book ID is required!"
            )
            return

        try:

            conn = self.connect_database()
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE library_management
                SET
                    title=%s,
                    author=%s,
                    publisher=%s,
                    price=%s,
                    no_of_copies=%s,
                    student_id=%s,
                    student_name=%s,
                    department=%s,
                    phone_no=%s,
                    issue_id=%s,
                    issue_date=%s,
                    due_date=%s,
                    return_date=%s,
                    fine=%s
                WHERE book_id=%s
                """,
                (
                    self.booktitle.get(),
                    self.author.get(),
                    self.publisher.get(),
                    self.price.get(),
                    self.nocopy.get(),
                    self.memeberid.get() or None,
                    self.name.get() or None,
                    self.department.get() or None,
                    self.phoneno.get() or None,
                    self.issueid.get() or None,
                    self.issuedate.get() or None,
                    self.duedate.get() or None,
                    self.returndate.get() or None,
                    self.fine.get() or 0,
                    self.bookid.get()
                )
            )

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Warning",
                    "No book found with this Book ID!"
                )
            else:

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Book details updated successfully!"
                )

            conn.close()

            self.fetchdata()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # FETCH DATA
    # =========================================================

    def fetchdata(self):

        try:

            conn = self.connect_database()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM library_management"
            )

            rows = cursor.fetchall()

            self.library.delete(
                *self.library.get_children()
            )

            for row in rows:
                self.library.insert(
                    "",
                    END,
                    values=row
                )

            conn.close()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # GET SELECTED RECORD
    # =========================================================

    def get_cursor(self, event=None):

        cursor_row = self.library.focus()

        if not cursor_row:
            return

        content = self.library.item(cursor_row)

        row = content["values"]

        if row:

            self.bookid.set(row[0])
            self.booktitle.set(row[1])
            self.author.set(row[2])
            self.publisher.set(row[3])
            self.price.set(row[4])
            self.nocopy.set(row[5])
            self.memeberid.set(row[6] if row[6] is not None else "")
            self.name.set(row[7] if row[7] is not None else "")
            self.department.set(row[8] if row[8] is not None else "")
            self.phoneno.set(row[9] if row[9] is not None else "")
            self.issueid.set(row[10] if row[10] is not None else "")
            self.issuedate.set(row[11] if row[11] is not None else "")
            self.duedate.set(row[12] if row[12] is not None else "")
            self.returndate.set(row[13] if row[13] is not None else "")
            self.fine.set(row[14] if row[14] is not None else "")

    # =========================================================
    # DELETE BOOK
    # =========================================================

    def deletebook(self):

        if self.bookid.get() == "":
            messagebox.showerror(
                "Error",
                "Book ID is required!"
            )
            return

        confirm = messagebox.askyesno(
            "Delete",
            "Are you sure you want to delete this book?"
        )

        if not confirm:
            return

        try:

            conn = self.connect_database()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM library_management
                WHERE book_id=%s
                """,
                (self.bookid.get(),)
            )

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Warning",
                    "No record found with this Book ID!"
                )

            else:

                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Book deleted successfully!"
                )

            conn.close()

            self.fetchdata()
            self.reset_librarydata(show_message=False)

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # =========================================================
    # ISSUE BOOK
    # =========================================================

    def issue_book(self):

        try:

            book_id = self.bookid.get()
            student_id = self.memeberid.get()
            student_name = self.name.get()
            issue_id = self.issueid.get()
            issue_date = self.issuedate.get()
            due_date = self.duedate.get()

            if (
                book_id == "" or
                student_id == "" or
                student_name == "" or
                issue_id == "" or
                issue_date == "" or
                due_date == ""
            ):

                messagebox.showerror(
                    "Error",
                    "Book ID, Student ID, Student Name, Issue ID, Issue Date and Due Date are required!"
                )
                return

            conn = self.connect_database()
            cursor = conn.cursor()

            # Check whether book exists
            cursor.execute(
                """
                SELECT no_of_copies
                FROM library_management
                WHERE book_id=%s
                """,
                (book_id,)
            )

            book = cursor.fetchone()

            if book is None:

                messagebox.showerror(
                    "Error",
                    "Book not found!"
                )

                conn.close()
                return

            try:
                copies = int(book[0])
            except:
                copies = 0

            if copies <= 0:

                messagebox.showerror(
                    "Error",
                    "No copies available for this book!"
                )

                conn.close()
                return

            # Check whether student already has an active book
            cursor.execute(
                """
                SELECT book_id
                FROM library_management
                WHERE student_id=%s
                AND return_date IS NULL
                AND issue_date IS NOT NULL
                """,
                (student_id,)
            )

            existing_issue = cursor.fetchone()

            if existing_issue:

                messagebox.showwarning(
                    "Warning",
                    "This student already has an issued book!"
                )

                conn.close()
                return

            # Update book record
            cursor.execute(
                """
                UPDATE library_management
                SET
                    no_of_copies=%s,
                    student_id=%s,
                    student_name=%s,
                    department=%s,
                    phone_no=%s,
                    issue_id=%s,
                    issue_date=%s,
                    due_date=%s,
                    return_date=NULL,
                    fine=0
                WHERE book_id=%s
                """,
                (
                    copies - 1,
                    self.memeberid.get(),
                    self.name.get(),
                    self.department.get(),
                    self.phoneno.get(),
                    self.issueid.get(),
                    self.issuedate.get(),
                    self.duedate.get(),
                    self.bookid.get()
                )
            )

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Book issued successfully!"
            )

            self.fetchdata()

        except Exception as e:

            messagebox.showerror(
                "Issue Book Error",
                str(e)
            )

    # =========================================================
    # RETURN BOOK
    # =========================================================

    def return_book(self):

        if (
            self.bookid.get() == "" or
            self.memeberid.get() == ""
        ):

            messagebox.showerror(
                "Error",
                "Book ID and Student ID are required!"
            )
            return

        try:

            conn = self.connect_database()
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT no_of_copies, issue_date, due_date
                FROM library_management
                WHERE book_id=%s
                AND student_id=%s
                AND issue_date IS NOT NULL
                AND return_date IS NULL
                """,
                (
                    self.bookid.get(),
                    self.memeberid.get()
                )
            )

            record = cursor.fetchone()

            if record is None:

                messagebox.showerror(
                    "Error",
                    "No active issue found for this book and student!"
                )

                conn.close()
                return

            copies = int(record[0])

            return_date = date.today()

            # Calculate fine
            fine_amount = 0

            if record[2]:

                try:

                    due_date = record[2]

                    if hasattr(due_date, "date"):
                        due_date = due_date.date()

                    overdue_days = (
                        return_date - due_date
                    ).days

                    if overdue_days > 0:
                        fine_amount = overdue_days * 5

                except:
                    fine_amount = 0

            cursor.execute(
                """
                UPDATE library_management
                SET
                    no_of_copies=%s,
                    return_date=%s,
                    fine=%s
                WHERE book_id=%s
                AND student_id=%s
                AND return_date IS NULL
                """,
                (
                    copies + 1,
                    return_date,
                    fine_amount,
                    self.bookid.get(),
                    self.memeberid.get()
                )
            )

            conn.commit()
            conn.close()

            self.returndate.set(
                str(return_date)
            )

            self.fine.set(
                str(fine_amount)
            )

            self.fetchdata()

            if fine_amount > 0:

                messagebox.showinfo(
                    "Book Returned",
                    f"Book returned successfully!\nFine: ₹{fine_amount}"
                )

            else:

                messagebox.showinfo(
                    "Success",
                    "Book returned successfully!"
                )

        except Exception as e:

            messagebox.showerror(
                "Return Book Error",
                str(e)
            )

    # =========================================================
    # RESET
    # =========================================================

    def reset_librarydata(self, show_message=True):

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

        if show_message:

            messagebox.showinfo(
                "Reset",
                "All fields have been cleared!"
            )


# =============================================================
# MAIN
# =============================================================

if __name__ == "__main__":

    root = Tk()

    obj = library(root)

    root.mainloop()