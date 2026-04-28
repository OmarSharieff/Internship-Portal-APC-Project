from models.user import User

class Instructor(User):
    def __init__(self, user_id, name, email, password, department, courses):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._department = department
        self._courses = courses

    def view_all_apps():
        pass

    def monitor_students():
        pass

    def generate_report():
        pass