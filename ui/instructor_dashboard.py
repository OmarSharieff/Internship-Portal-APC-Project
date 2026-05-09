import tkinter as tk

class InstructorDashboard:
    def __init__(self, user):
        self.instructor_dashboard  = tk.Tk()
        self.instructor_dashboard.title(f"Instructor Dashboard - {user[1]}")
        self.instructor_dashboard.geometry("350x250")

        
        self.instructor_dashboard.resizable(False, False) 
        
        
        container = tk.Frame(self.instructor_dashboard)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        
        tk.Label(container, text=f"Instructor: {user[1]}").pack(pady=20)

        tk.Button(container, text="Monitor Students", width=25).pack(pady=10)
        tk.Button(container, text="Application Outcomes", width=25).pack(pady=10)

        self.instructor_dashboard.mainloop()