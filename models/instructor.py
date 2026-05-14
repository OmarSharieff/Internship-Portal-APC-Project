from models.user import User


class Instructor(User):
    def __init__(self, user_id, name, email,
                 password, department, courses):

        super().__init__(user_id, name, email, password)

        self._department = department
        self._courses = courses

    def view_all_apps(self, all_applications):
        return list(all_applications)

    def monitor_students(self, all_applications):

        report = {}

        for app in all_applications:

            sid = app.get_student_id()

            if sid not in report:
                report[sid] = {
                    "student_id": sid,
                    "total": 0,
                    "pending": 0,
                    "under_review": 0,
                    "approved": 0,
                    "rejected": 0
                }

            report[sid]["total"] += 1
            report[sid][app.get_status()] += 1

        return list(report.values())

    def generate_report(self, all_applications):

        report = {
            "total_applications": len(all_applications),
            "approved": 0,
            "rejected": 0,
            "pending": 0,
            "under_review": 0
        }

        for app in all_applications:
            report[app.get_status()] += 1

        return report

    def __str__(self):
        return f"Instructor({self._name})"