from user import User
from internship import Internship
from datetime import date

class Company(User):
    def __init__(self, user_id, name, email, password, industry, location):
        super().__init__(user_id, name, email, password) #resuing parent initialization
        self._industry = industry
        self._location = location

    def post_intern(self, title, description, deadline, all_internships: list):
        #business logic
        '''
        step1: check for already existing internship and valid deadline
        step2: otherwise, post an internship
        '''
        duplicate_internship = [
            i for i in all_internships
            if i._company_id == self._user_id and i._title = title
        ]
        if len(duplicate) > 0:
            return "You already posted an internship with this title!"
        if deadline < date.today().isoformat():
            return "Deadline cannot be in the past!"
        
        return Internship(title=title, description=description, company_id=self._user_id, deadline=deadline)

    def view_apps():
        pass

    def approve():
        pass

    def reject():
        pass
