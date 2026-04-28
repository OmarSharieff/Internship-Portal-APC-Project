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
        if len(duplicate_internship) > 0:
            return "You already posted an internship with this title!"
        if deadline < date.today().isoformat():
            return "Deadline cannot be in the past!"
        
        return Internship(title=title, description=description, company_id=self._user_id, deadline=deadline)

    def view_apps(self, all_applications: list, all_internships: list):
        #business logic
        '''
        step1: fetch all internships belonging to this company
        step2: filter applications for the fetched internships
        '''
        my_internship_ids = [i._internship_id for i in all_internships
                             if i._company_id == self._user_id]
        
        my_apps = [a for a in all_internships
                   if a._intership_id in my_internship_ids]
        
        return my_apps

    def approve(self, application, notes=""):
        # business logic
        '''
        step1: check application status and return accordingly
        step2: otherwise, approve application and assign notes
        '''
        if application._status == "approved":
            return "Application is already approved"
        if application._status == "rejected":
            return "Cannot approved already rejected application"
        
        application._status == "approved"
        application._notes = notes
        return application
        


    def reject(self, application, notes=""):
        # business logic is inverse of approve()
        if application._status == "rejected":
            return "Application is already rejected"
        if application._status == "accepted":
            return "Cannot reject already approved application"
        
        application._status = "rejected"
        application._notes = notes
        return application
