from models.student import Student
from models.company import Company
from models.instructor import Instructor
from models.internship import Internship


print("========== SETUP ==========")

student = Student(
    1,
    "Alice",
    "alice@gmail.com",
    "pass123",
    "MIT",
    3.8,
    "resume.pdf"
)

company = Company(
    2,
    "TechCorp",
    "tech@corp.com",
    "pass123",
    "Software",
    "NYC"
)

instructor = Instructor(
    3,
    "Dr. Smith",
    "smith@uni.com",
    "pass123",
    "CS Department",
    ["OOP", "DSA"]
)

all_internships = []
all_applications = []


print("\n========== LOGIN TESTS ==========")

print(student.login("alice@gmail.com", "pass123"))
print(company.login("tech@corp.com", "wrong"))


print("\n========== POST INTERNSHIP TESTS ==========")

internship1 = company.post_intern(
    "Backend Intern",
    "API Development",
    "2027-12-31",
    all_internships
)

print(type(internship1))

all_internships.append(internship1)

duplicate = company.post_intern(
    "Backend Intern",
    "Duplicate",
    "2027-12-31",
    all_internships
)

print(duplicate)

expired = company.post_intern(
    "Expired Intern",
    "Bad",
    "2020-01-01",
    all_internships
)

print(expired)


print("\n========== VIEW INTERNSHIPS ==========")

available = student.view_intern(all_internships)

print(len(available))


print("\n========== APPLY TESTS ==========")

app = student.apply(internship1, all_applications)

print(type(app))

all_applications.append(app)

duplicate_apply = student.apply(internship1, all_applications)

print(duplicate_apply)


print("\n========== VIEW MY APPLICATIONS ==========")

my_apps = student.view_apps(all_applications)

print(len(my_apps))


print("\n========== COMPANY VIEW APPS ==========")

company_apps = company.view_apps(
    all_applications,
    all_internships
)

print(len(company_apps))


print("\n========== APPROVE TEST ==========")

result = company.approve(
    app,
    notes="Excellent resume"
)

print(app.get_status())


print("\n========== DOUBLE APPROVE ==========")

print(company.approve(app))


print("\n========== REJECT AFTER APPROVE ==========")

print(company.reject(app))


print("\n========== APPLICATION STATUS TEST ==========")

print(app.update_status("approved"))

print(app.update_status("invalid_status"))


print("\n========== INSTRUCTOR TESTS ==========")

all_apps = instructor.view_all_apps(all_applications)

print(len(all_apps))

monitor = instructor.monitor_students(all_applications)

print(monitor)

report = instructor.generate_report(all_applications)

print(report)


print("\n========== CLOSE INTERNSHIP ==========")

print(internship1.close())

print(internship1.close())


print("\n========== APPLY TO CLOSED INTERNSHIP ==========")

closed_result = student.apply(
    internship1,
    all_applications
)

print(closed_result)


print("\n========== GET DETAILS ==========")

print(internship1.get_details())


print("\n========== APPROVED CHECK ==========")

print(app.get_approved())


print("\n========== ALL TESTS COMPLETED ==========")