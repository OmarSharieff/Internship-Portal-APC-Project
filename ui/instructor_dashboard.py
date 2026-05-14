import tkinter as tk

from database.db_helper import execute_query


class InstructorDashboard:

    def __init__(self, user):

        self.root = tk.Tk()

        self.root.title(f"Instructor Dashboard - {user[1]}")
        self.root.geometry("500x400")

        container = tk.Frame(self.root)
        container.pack(pady=30)

        tk.Label(
            container,
            text=f"Instructor: {user[1]}",
            font=("Arial", 14)
        ).pack(pady=20)

        tk.Button(
            container,
            text="View All Applications",
            width=25,
            command=self.view_all
        ).pack(pady=10)

        self.root.mainloop()

    def view_all(self):

        query = """
        SELECT users.name,
               internships.title,
               applications.status
        FROM applications
        JOIN users
        ON applications.student_id = users.user_id
        JOIN internships
        ON applications.internship_id = internships.internship_id
        """

        apps = execute_query(query, fetch=True)

        window = tk.Toplevel(self.root)
        window.geometry("600x400")

        for app in apps:

            text = (
                f"Student: {app[0]} | "
                f"Internship: {app[1]} | "
                f"Status: {app[2]}"
            )

            tk.Label(window, text=text).pack(pady=5)