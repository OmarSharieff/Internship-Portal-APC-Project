import tkinter as tk

class CompanyDashboard:
    def __init__(self, user):
        self.company_dashboard = tk.Tk()
        self.company_dashboard.title(f"Company Dashboard - {user[1]}")
        self.company_dashboard.geometry("350x250")

        
        # Avoid resize 
        self.company_dashboard.resizable(False, False) 
        
    
        container = tk.Frame(self.company_dashboard)
        container.place(relx=0.5, rely=0.5, anchor="center")
    
        tk.Label(container, text=f"Company: {user[1]}").pack(pady=20)

    
        tk.Button(container, text="Post Internship", width=25).pack(pady=10)
        tk.Button(container, text="Approve/Reject Applicants", width=25).pack(pady=10)

        self.company_dashboard.mainloop()