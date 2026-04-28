from user import User

class Student(User):
    def __init__(self, user_id, name, email, password, student_id, university, gpa, resume):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._student_id = student_id
        self._university = university
        self._gpa = gpa
        self._resume = resume

    def view_intern():
        pass

    def apply():
        pass

    def view_apps():
        pass