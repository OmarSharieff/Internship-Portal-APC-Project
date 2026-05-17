from models.user import User
from datetime import date
from models.application import Application

class Student(User):
    def __init__(self, user_id, name, email, password, university, gpa, resume):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._university = university
        self._gpa = gpa
        self._resume = resume

    def view_intern(self, all_internships: list):
        # returns only open internsips which haven't passed their deadline
        # NOTE: isoformat() is used for comparing dates as strings. Do not change the format otherwise it will break the logic!
        return [i for i in all_internships if i._is_open and i._deadline >= date.today().isoformat()]
        
    def apply(self, internship, all_applications: list):


        already_applied = any(a._student_id == self._user_id and a._internship_id == internship._internship_id for a in all_applications)
        
        if already_applied:
            return "Already applied to this internship."
        if not internship._is_open:
            return "This internship is closed."
        if internship._deadline < date.today().isoformat():
            return "Deadline has passed."

        #NOTE: app_id=None is only for test purposes.
        return Application(app_id=None, student_id=self._user_id, internship_id=internship._internship_id)
        

    def view_apps(self, all_applications: list):
        # filtering applications that belong to a particular student (sorted by most recent)
        my_apps= [a for a in all_applications if a._student_id == self._user_id]
        return sorted(my_apps, key=lambda a: a._applied_at, reverse=True) #ordering by recently applied