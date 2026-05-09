import tkinter as tk


class StudentDashboard:
    def __init__(self, user):
        self.student_dashboard = tk.Tk()
        self.student_dashboard.title(f"Student Dashboard - {user[1]}")
        self.student_dashboard.geometry("350x250")
        self.student_dashboard.resizable(False, False) 
        

    
        container = tk.Frame(self.student_dashboard) 
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(container, text=f"Welcome, {user[1]}").pack(pady=20)

        
        tk.Button(container, text="View Internships", width=20).pack(pady=10)
        tk.Button(container, text="Apply", width=20).pack(pady=10)
        tk.Button(container, text="Track Application Status", width=20).pack(pady=10)

        self.student_dashboard.mainloop()