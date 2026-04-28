from user import User

class Company(User):
    def __init__(self, user_id, name, email, password, company_id, company_name, industry, location):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._company_id = company_id
        self._company_name = company_name
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
