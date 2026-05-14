import tkinter as tk
from tkinter import messagebox

from database.db_helper import (
    insert_internship,
    fetch_company_applications,
    update_application_status
)


class CompanyDashboard:

    def __init__(self, user):

        self.user = user

        self.root = tk.Tk()

        self.root.title(f"Company Dashboard - {user[1]}")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        container = tk.Frame(self.root)
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            container,
            text=f"Company: {user[1]}",
            font=("Arial", 14)
        ).pack(pady=20)

        tk.Button(
            container,
            text="Post Internship",
            width=25,
            command=self.post_internship
        ).pack(pady=10)

        tk.Button(
            container,
            text="Approve / Reject Applicants",
            width=25,
            command=self.manage_applications
        ).pack(pady=10)

        self.root.mainloop()

    def post_internship(self):

        window = tk.Toplevel(self.root)

        window.title("Post Internship")
        window.geometry("400x350")

        tk.Label(window, text="Title").pack()
        title_entry = tk.Entry(window, width=30)
        title_entry.pack(pady=5)

        tk.Label(window, text="Description").pack()
        desc_entry = tk.Entry(window, width=30)
        desc_entry.pack(pady=5)

        tk.Label(window, text="Deadline (YYYY-MM-DD)").pack()
        deadline_entry = tk.Entry(window, width=30)
        deadline_entry.pack(pady=5)

        def submit():

            try:

                insert_internship(
                    title_entry.get(),
                    desc_entry.get(),
                    self.user[0],
                    deadline_entry.get()
                )

                messagebox.showinfo(
                    "Success",
                    "Internship posted successfully."
                )

                window.destroy()

            except Exception as e:

                messagebox.showerror(
                    "Error",
                    str(e)
                )

        tk.Button(
            window,
            text="Post",
            command=submit
        ).pack(pady=20)

    def manage_applications(self):

        apps = fetch_company_applications(self.user[0])

        window = tk.Toplevel(self.root)
        window.title("Applications")
        window.geometry("600x400")

        if not apps:

            tk.Label(
                window,
                text="No applications found."
            ).pack(pady=20)

            return

        for app in apps:

            frame = tk.Frame(window)
            frame.pack(pady=10)

            text = (
                f"App ID: {app[0]} | "
                f"Student: {app[1]} | "
                f"Internship: {app[2]} | "
                f"Status: {app[3]}"
            )

            tk.Label(frame, text=text).pack(side=tk.LEFT)

            tk.Button(
                frame,
                text="Approve",
                command=lambda a=app[0]: self.approve(a, window)
            ).pack(side=tk.LEFT, padx=5)

            tk.Button(
                frame,
                text="Reject",
                command=lambda a=app[0]: self.reject(a, window)
            ).pack(side=tk.LEFT, padx=5)

    def approve(self, app_id, window):

        update_application_status(app_id, "approved")

        messagebox.showinfo(
            "Success",
            "Application approved."
        )

        window.destroy()

    def reject(self, app_id, window):

        update_application_status(app_id, "rejected")

        messagebox.showinfo(
            "Success",
            "Application rejected."
        )

        window.destroy()