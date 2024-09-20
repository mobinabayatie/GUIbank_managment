import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.mainLabel = tk.Label(self.root, text="Login", font=("Arial", 24, "bold"))
        self.mainLabel.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username:", font=("Arial", 14))
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.root, textvariable=self.username, font=("Arial", 14))
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:", font=("Arial", 14))
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*", textvariable=self.password, font=("Arial", 14))
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", font=("Arial", 14), command=self.check_login)
        self.login_button.pack(pady=20)

        self.addemp_button = tk.Button(self.root, text="Add new employee", font=("Arial", 14))
        self.addemp_button.pack(pady=10)

    def check_login(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employee WHERE emp_username=? AND emp_password=?",
                           (self.username.get(), self.password.get()))
            result = cursor.fetchone()

            if result:
                tk.messagebox.showinfo("Login Success", "Welcome to the Bank Management System")
                self.root.destroy()
                self.open_main_app()
            else:
                tk.messagebox.showerror("Login Error", "Invalid username or password")

    def open_main_app(self):  #open main window after log in
        # self.root.withdraw()
        new_root = tk.Toplevel()
        app = User(new_root)
        new_root.mainloop()


class User():
    def __init__(self, root):
        self.root = root
        self.root.title("Bank management")
        self.root.geometry("1400x650+0+0")
        self.mainLabel = tk.Label(self.root, bd=5, relief="groove", text="Bank management system",
                                  font=("Arial", 40, "bold"), bg="green",
                                  fg="white")
        self.mainLabel.pack(side=tk.TOP, fill="x")
        # ----variables---
        self.usernationalID = tk.StringVar()
        self.accountnumber = tk.StringVar()
        self.password = tk.IntVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.balance = tk.IntVar()
        self.status = tk.StringVar()
        self.searchtype = tk.StringVar()
        self.searchentry = tk.StringVar()

        # frame1
        self.fram1 = tk.Frame(self.root, bg="white", bd=5, relief="ridge")
        self.fram1.place(x=10, y=80, width=370, height=550)

        self.idLable = tk.Label(self.fram1, padx=5, text=" National ID:", bg="white", fg="green",
                                font=("Arial", 14, "bold"),
                                pady=10)
        self.idLable.grid(row=0, column=0)
        self.identry = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.usernationalID)
        self.identry.grid(row=0, column=1, pady=10)

        self.nameLable = tk.Label(self.fram1, padx=5, text="Account number:", bg="white", fg="green",
                                  font=("Arial", 14, "bold"),
                                  pady=10)
        self.nameLable.grid(row=1, column=0)
        self.nameentry = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.accountnumber)
        self.nameentry.grid(row=1, column=1, pady=10)

        self.user_firastnameLable = tk.Label(self.fram1, padx=5, text="First name:", bg="white", fg="green",
                                             font=("Arial", 14, "bold"),
                                             pady=10)
        self.user_firastnameLable.grid(row=2, column=0)
        self.user_firastnameentry = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.firstname)
        self.user_firastnameentry.grid(row=2, column=1, pady=10)

        self.user_lastnameLable = tk.Label(self.fram1, padx=5, text="Last name:", bg="white", fg="green",
                                           font=("Arial", 14, "bold"),
                                           pady=10)
        self.user_lastnameLable.grid(row=3, column=0)
        self.user_lastnameentry = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.lastname)
        self.user_lastnameentry.grid(row=3, column=1, pady=10)

        self.passwordLable = tk.Label(self.fram1, padx=5, text="Password:", bg="white", fg="green",
                                      font=("Arial", 14, "bold"),
                                      pady=10)
        self.passwordLable.grid(row=4, column=0)
        self.passwordentry = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.password)
        self.passwordentry.grid(row=4, column=1, pady=10)

        self.balanceLable = tk.Label(self.fram1, padx=5, text="Balance:", bg="white", fg="green",
                                     font=("Arial", 14, "bold"),
                                     pady=10)
        self.balanceLable.grid(row=5, column=0)
        self.balanceentry = tk.Entry(self.fram1, font=("Arial", 14), width=15, textvariable=self.balance)
        self.balanceentry.grid(row=5, column=1, pady=10)

        self.statusLable = tk.Label(self.fram1, padx=5, text="Status:", bg="white", fg="green",
                                    font=("Arial", 14, "bold"),
                                    pady=10)
        self.statusLable.grid(row=6, column=0)
        self.statusentry = ttk.Combobox(self.fram1, font=("Arial", 14), width=13, state="readonly",
                                        textvariable=self.status)
        self.statusentry['values'] = ("Active", "DiActive")
        self.statusentry.grid(row=6, column=1, pady=10)

        # -----Button frame-----
        self.buttonframe = tk.Frame(self.fram1, bg="white", bd=5, relief="raised")
        self.buttonframe.place(x=10, y=380, width=340, height=150)

        self.addbutton = tk.Button(self.buttonframe, width=10, text="Add", font=("Arial", 14, "bold"), command=self.add)
        self.addbutton.grid(row=0, column=0, padx=10, pady=10)

        # other buttons
        self.updatebutton = tk.Button(self.buttonframe, width=10, text="Update", font=("Arial", 14, "bold"),
                                      command=self.update)
        self.updatebutton.grid(row=0, column=1, padx=10, pady=10)

        self.deletebutton = tk.Button(self.buttonframe, width=10, text="Delete", font=("Arial", 14, "bold"),
                                      command=self.delete)
        self.deletebutton.grid(row=1, column=0, padx=10, pady=10)

        self.clearbutton = tk.Button(self.buttonframe, width=10, text="Clear", font=("Arial", 14, "bold"),
                                     command=self.clear)
        self.clearbutton.grid(row=1, column=1, padx=10, pady=10)

        # frame2
        self.fram2 = tk.Frame(self.root, bg="white", bd=5, relief="ridge")
        self.fram2.place(x=400, y=80, width=870, height=550)

        self.searchLable = tk.Label(self.fram2, padx=5, text="Search By:", bg="white", fg="green",
                                    font=("Arial", 14, "bold"),
                                    pady=10)
        self.searchLable.grid(row=0, column=0)
        self.searchtype = ttk.Combobox(self.fram2, font=("Arial", 14), width=13, state="readonly",
                                       textvariable=self.searchtype)
        self.searchtype['values'] = (" National ID", "Account number")
        self.searchtype.grid(row=0, column=1, pady=10)

        self.searchentry = tk.Entry(self.fram2, font=("Arial", 14), width=15, textvariable=self.searchentry)
        self.searchentry.grid(row=0, column=2, pady=10, padx=10)

        self.searchbutton = tk.Button(self.fram2, width=10, text="Search", font=("Arial", 14, "bold"),
                                      command=self.search)
        self.searchbutton.grid(row=0, column=3, padx=5, pady=10)

        self.showbutton = tk.Button(self.fram2, width=10, text="Display All", font=("Arial", 14, "bold"),
                                    command=self.showall)
        self.showbutton.grid(row=0, column=4, padx=10, pady=10)

        # -----table frame-----
        self.tableframe = tk.Frame(self.fram2, bg="green", bd=5, relief="ridge")
        self.tableframe.place(x=10, y=80, width=840, height=450)

        self.x_scrol = tk.Scrollbar(self.tableframe, orient="horizontal")
        self.x_scrol.pack(side=tk.BOTTOM, fill="x")

        self.y_scrol = tk.Scrollbar(self.tableframe, orient="vertical")
        self.y_scrol.pack(side=tk.RIGHT, fill="y")

        self.table = ttk.Treeview(self.tableframe, columns=(
            "ID", "National ID", "Account Number", "Firstname", "Lastname", "Balance", "Status"),
                                  xscrollcommand=self.x_scrol,
                                  yscrollcommand=self.y_scrol)
        self.x_scrol.config(command=self.table.xview())
        self.y_scrol.config(command=self.table.yview())

        self.table.heading("ID", text="ID")
        self.table.heading("National ID", text="National ID")
        self.table.heading("Account Number", text="Account Number")
        self.table.heading("Firstname", text="Firstname")
        self.table.heading("Lastname", text="Lastname")
        self.table.heading("Balance", text="Balance")
        self.table.heading("Status", text="Status")
        self.table['show'] = "headings"

        self.table.column("National ID", width=100)
        self.table.column("Account Number", width=100)
        self.table.column("Firstname", width=100)
        self.table.column("Lastname", width=100)
        self.table.column("Balance", width=100)
        self.table.column("Status", width=100)

        self.table.pack(fill="both", expand=1)

    def add(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO user (national_ID, account_number, firstname, lastname, password, balance, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (self.usernationalID.get(), self.accountnumber.get(), self.firstname.get(),
                            self.lastname.get(), self.password.get(), self.balance.get(), self.status.get()))
            connection.commit()
            tk.messagebox.showinfo("Success", "Data inserted successfully")
            self.get_data()
            connection.close()

    def get_data(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""select * from user""")
            data = cursor.fetchall()
            if len(data) > 0:
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert('', tk.END, values=i)
                connection.commit()
            connection.close()

    def clear(self):
        self.usernationalID.set("")
        self.accountnumber.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.password.set(0)
        self.balance.set(0)
        self.status.set("")

    def update(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"select ID from user where national_ID=?", (self.usernationalID.get(),))
            id = cursor.fetchone()[0]
            cursor.execute("update user set national_ID=?, account_number=? , firstname=?,"
                           " lastname=? , password=? , balance=? , status=? where ID=?", (self.usernationalID.get(),
                                                                                          self.accountnumber.get(),
                                                                                          self.firstname.get(),
                                                                                          self.lastname.get(),
                                                                                          self.password.get(),
                                                                                          self.balance.get(),
                                                                                          self.status.get(), id))
            connection.commit()
            tk.messagebox.showinfo("Success", "Data updated successfully")
            self.get_data()
            connection.close()

    def delete(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"select ID from user where national_ID=?", (self.usernationalID.get(),))
            id = cursor.fetchone()[0]
            cursor.execute("delete from user where ID =? ", (id,))
            connection.commit()
            tk.messagebox.showinfo("Success", "Data deleted successfully")
            self.get_data()
        connection.close()

    def search(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            if self.searchtype.get() == " National ID":
                cursor.execute("SELECT * FROM user WHERE national_ID=?", (self.searchentry.get(),))
            elif self.searchtype.get() == "Account number":
                cursor.execute("SELECT * FROM user WHERE account_number=?", (self.searchentry.get(),))

            rows = cursor.fetchall()
            if len(rows) > 0:
                self.table.delete(*self.table.get_children())
                for j in rows:
                    self.table.insert('', tk.END, values=j)
                connection.commit()
            else:
                tk.messagebox.showerror("Error", "No Data Found!")
            connection.close()

    def showall(self):
        with sqlite3.connect("C:\\Users\\HK\\Desktop\\GUIbank.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""select * from user""")
            data = cursor.fetchall()
            if len(data) > 0:
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert('', tk.END, values=i)
                connection.commit()
            else:
                tk.messagebox.showerror("Error", "NO Data Found!")

            connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    # obj = User(root)
    root.mainloop()
