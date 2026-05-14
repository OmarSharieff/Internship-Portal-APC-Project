import tkinter as tk
from tkinter import messagebox

from database.db_helper import fetch_user

from ui.student_dashboard import StudentDashboard
from ui.company_dashboard import CompanyDashboard
from ui.instructor_dashboard import InstructorDashboard


class Login:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Login")
        self.root.geometry("350x250")
        self.root.resizable(False, False)

        container = tk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Email").pack(pady=(0, 5))

        self.email_entry = tk.Entry(container, width=30)
        self.email_entry.pack(pady=(0, 10))

        tk.Label(container, text="Password").pack(pady=(0, 5))

        self.password_entry = tk.Entry(container, show="*", width=30)
        self.password_entry.pack(pady=(0, 15))

        tk.Button(
            container,
            text="Login",
            width=15,
            command=self.login
        ).pack()

    def login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        user = fetch_user(email, password)

        if not user:
            messagebox.showerror(
                "Login Failed",
                "Invalid email or password."
            )
            return

        self.open_dashboard(user)

    def open_dashboard(self, user):

        role = user[4].lower()

        self.root.destroy()

        if role == "student":
            StudentDashboard(user)

        elif role == "company":
            CompanyDashboard(user)

        elif role == "instructor":
            InstructorDashboard(user)

        else:
            messagebox.showerror(
                "Error",
                f"Unknown role: {role}"
            )