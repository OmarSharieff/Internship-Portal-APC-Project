# THIS IS A LLM GENERATED TESTING SCRIPT!

from models.student import Student
from models.company import Company
from models.instructor import Instructor
from models.internship import Internship


# --- Setup dummy data ---
student = Student(1, "Alice", "alice@gmail.com", "pass123", "MIT", 3.8, "resume.pdf")
company = Company(2, "TechCorp", "tech@corp.com", "pass123", "Software", "NYC")
instructor = Instructor(3, "Dr. Smith", "smith@uni.com", "pass123", "CS Department", ["OOP", "DSA"])

internship1 = Internship(1, "Backend Intern", "Work on APIs", 2, "2027-12-31", True)
internship2 = Internship(2, "Frontend Intern", "Work on UI", 2, "2024-01-01", True)  # expired deadline

all_internships = [internship1, internship2]
all_applications = []

# --- Test view_intern() ---
print("=== Available Internships ===")
available = student.view_intern(all_internships)
print(f"Expected 1, Got: {len(available)}")  # internship2 should be filtered out

# --- Test apply() ---
print("\n=== Apply to Internship ===")
app = student.apply(internship1, all_applications)
print(f"Expected Application object, Got: {type(app)}")
all_applications.append(app)

# --- Test duplicate apply() ---
print("\n=== Duplicate Application ===")
duplicate = student.apply(internship1, all_applications)
print(f"Expected error string, Got: {duplicate}")

# --- Test view_apps() ---
print("\n=== Student View Apps ===")
my_apps = student.view_apps(all_applications)
print(f"Expected 1 app, Got: {len(my_apps)}")

# --- Test company view_apps() ---
print("\n=== Company View Apps ===")
company_apps = company.view_apps(all_applications, all_internships)
print(f"Expected 1 app, Got: {len(company_apps)}")

# --- Test approve() ---
print("\n=== Approve Application ===")
result = company.approve(app, notes="Great candidate!")
print(f"Expected approved status, Got: {app._status}")

# --- Test double approve() ---
print("\n=== Double Approve ===")
result = company.approve(app)
print(f"Expected error string, Got: {result}")

# --- Test internship close() ---
print("\n=== Close Internship ===")
print(internship1.close())
print(internship1.close())  # should return already closed message