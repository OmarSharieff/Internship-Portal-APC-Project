from datetime import date
from models.user import User
from models.application import Application


class Student(User):
    def __init__(self, user_id, name, email,
                 password, university, gpa, resume):

        super().__init__(user_id, name, email, password)

        if gpa < 0 or gpa > 4:
            raise ValueError("Invalid GPA")

        self._university = university
        self._gpa = gpa
        self._resume = resume

    def view_intern(self, all_internships):
        return [
            i for i in all_internships
            if i.is_open() and i.get_deadline() >= date.today().isoformat()
        ]

    def apply(self, internship, all_applications):

        already_applied = [
            a for a in all_applications
            if a.get_student_id() == self._user_id and
               a.get_internship_id() == internship.get_id()
        ]

        if len(already_applied) > 0:
            return "Already applied to this internship."

        if not internship.is_open():
            return "This internship is closed."

        if internship.get_deadline() < date.today().isoformat():
            return "Deadline has passed."

        return Application(
            student_id=self._user_id,
            internship_id=internship.get_id()
        )

    def view_apps(self, all_applications):

        my_apps = [
            a for a in all_applications
            if a.get_student_id() == self._user_id
        ]

        return sorted(
            my_apps,
            key=lambda a: a._applied_at,
            reverse=True
        )

    def __str__(self):
        return f"Student({self._name})"