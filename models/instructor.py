# this is a read only class

from models.user import User

class Instructor(User):
    def __init__(self, user_id, name, email, password, department, courses):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._department = department
        self._courses = courses

    def view_all_apps(self, all_applications: list):
        # aim to return all applications for all students
        return [a for a in all_applications]

    def monitor_students(self, all_applications: list):
        # return every student's application status so far (per student status)
        student_ids = [a._student_id for a in all_applications]
        unique_students = list(set(student_ids)) # no repeated student id

        report = []
        for student_id in unique_students:
            student_application = [a for a in all_applications if a._student_id == student_id]
            statuses = {
                "student_id"  : student_id,
                "total"       : len(student_application),
                "pending"     : len([a for a in student_application if a._status == "pending"]),
                "under_review": len([a for a in student_application if a._status == "under_review"]),
                "approved"    : len([a for a in student_application if a._status == "approved"]),
                "rejected"    : len([a for a in student_application if a._status == "rejected"])
            }
            report.append(statuses)
        return report

    def generate_report(self, all_applications: list):
        # return entire portal's application status
        approved = [a for a in all_applications if a._status == "approved"]
        rejected = [a for a in all_applications if a._status == "rejected"]
        pending = [a for a in all_applications if a._status == "pending"]
        reviewed = [a for a in all_applications if a._status == "under_review"]
        return {
            "total_applications" : len(all_applications),
            "approved"           : len(approved),
            "rejected"           : len(rejected),
            "pending"            : len(pending),
            "under_review"       : len(reviewed)
        }