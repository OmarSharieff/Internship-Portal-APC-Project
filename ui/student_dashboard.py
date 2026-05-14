import tkinter as tk
from tkinter import messagebox

from database.db_helper import (
    fetch_internships,
    insert_application,
    fetch_student_applications
)


class StudentDashboard:

    def __init__(self, user):

        self.user = user

        self.root = tk.Tk()

        self.root.title(f"Student Dashboard - {user[1]}")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        container = tk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            container,
            text=f"Welcome, {user[1]}",
            font=("Arial", 14)
        ).pack(pady=20)

        tk.Button(
            container,
            text="View Internships",
            width=25,
            command=self.view_internships
        ).pack(pady=10)

        tk.Button(
            container,
            text="Apply",
            width=25,
            command=self.apply_to_internship
        ).pack(pady=10)

        tk.Button(
            container,
            text="Track Applications",
            width=25,
            command=self.track_applications
        ).pack(pady=10)

        self.root.mainloop()

    def view_internships(self):

        internships = fetch_internships()

        window = tk.Toplevel(self.root)
        window.title("Available Internships")
        window.geometry("500x300")

        for internship in internships:

            text = (
                f"ID: {internship[0]} | "
                f"{internship[1]} | "
                f"Deadline: {internship[4]}"
            )

            tk.Label(window, text=text).pack(pady=5)

    def apply_to_internship(self):

        internships = fetch_internships()

        window = tk.Toplevel(self.root)
        window.title("Apply")
        window.geometry("400x300")

        tk.Label(
            window,
            text="Enter Internship ID"
        ).pack(pady=10)

        internship_entry = tk.Entry(window)
        internship_entry.pack(pady=10)

        for internship in internships:

            tk.Label(
                window,
                text=f"{internship[0]} - {internship[1]}"
            ).pack()

        def submit():

            try:
                internship_id = int(internship_entry.get())

                insert_application(
                    self.user[0],
                    internship_id
                )

                messagebox.showinfo(
                    "Success",
                    "Application submitted successfully."
                )

                window.destroy()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        tk.Button(
            window,
            text="Apply",
            command=submit
        ).pack(pady=20)

    def track_applications(self):

        apps = fetch_student_applications(self.user[0])

        window = tk.Toplevel(self.root)
        window.title("My Applications")
        window.geometry("500x300")

        if not apps:
            tk.Label(
                window,
                text="No applications found."
            ).pack(pady=20)

            return

        for app in apps:

            text = (
                f"App ID: {app[0]} | "
                f"Internship: {app[1]} | "
                f"Status: {app[2]} | "
                f"Applied At: {app[3]}"
            )

            tk.Label(window, text=text).pack(pady=5)