import tkinter as tk
from tkinter import messagebox
import sqlite3
from database.db_setup import PATH


from ui.student_dashboard import StudentDashboard
from ui.company_dashboard import CompanyDashboard
from ui.instructor_dashboard import InstructorDashboard


class Login:
    def __init__(self):
        self.login_screen = tk.Tk()
        self.login_screen.title('Login Page')
        self.login_screen.geometry("350x250") 
        
        
        self.login_screen.resizable(False, False)
        

        # keep info in center
        container = tk.Frame(self.login_screen)
        container.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(container, text='Username').pack(pady=(0, 5))
        self.username_entry = tk.Entry(container)
        self.username_entry.pack(pady=(0, 10))
        
        tk.Label(container, text='Password').pack(pady=(0, 5))
        self.password_entry = tk.Entry(container, show='*')
        self.password_entry.pack(pady=(0, 15))

        self.login_btn = tk.Button(container, text='Login', command=self.login, width=15)
        self.login_btn.pack()

        self.login_screen.mainloop()

    def login(self):
        con = sqlite3.connect(PATH)
        cursor = con.cursor()

        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute('SELECT * FROM users WHERE name=? AND password=?',(username,password))
        user = cursor.fetchone()

        if user:
            self.open_dashboard(user)
        else:
            messagebox.showerror('Unable to login','Invalid username or password')

        con.close()

    def open_dashboard(self, user):
        self.login_screen.destroy()
        role = user[4].lower() 

        if role == 'student':
            StudentDashboard(user)
        elif role == 'company':
            CompanyDashboard(user)
        elif role == 'instructor':
            InstructorDashboard(user)
        else:
            messagebox.showerror("Error", f"Unknown role found: {role}")