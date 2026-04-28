from user import User

class Company(User):
    def __init__(self, user_id, name, email, password, industry, location):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._industry = industry
        self._location = location

    def post_intern():
        pass

    def view_apps():
        pass

    def approve():
        pass

    def reject():
        pass
