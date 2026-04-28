from user import User
from datetime import date
from application import Application

class Student(User):
    def __init__(self, user_id, name, email, password, university, gpa, resume):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._university = university
        self._gpa = gpa
        self._resume = resume

    def view_intern(self, all_internships: list):
        # This business logic code is written prior to sqlite3 schema setup assuming Internship class to have deadline and 'is_open' attributes.
        # NOTE: isoformat() is used for comparing date. Do not change the format otherwise it will break the logic!
        return [i for i in all_internships if i.is_open and i.deadline >= date.today().isoformat()]
        
    def apply(self, internship, all_applications: list):
        already_applied = [
            a for a in all_applications
            if a.student_id == self.user_id and a.internship_id == internship.internship_id
        ]
        if len(already_applied) > 0:
            return "Already applied to this internship."
        if not internship.is_open:
            return "This internship is closed."
        if internship.deadline < date.today().isoformat():
            return "Deadline has passed."

        return Application(student_id=self.user_id, internship_id=internship.internship_id)
        

    def view_apps():
        pass