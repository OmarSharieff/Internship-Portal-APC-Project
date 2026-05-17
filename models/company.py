from models.user import User
from models.internship import Internship
from datetime import date


class Company(User):
    def __init__(self, user_id, name, email, password, industry, location):
        super().__init__(user_id, name, email, password)
        self._industry = industry
        self._location = location

    def post_intern(self, title, description, deadline, all_internships: list):
        # avoiding posting the same internship multiple times
        duplicate = [
            i for i in all_internships
            if i._company_id == self._user_id and i._title == title
        ]

        if duplicate:
            return "Internship already exists."

        # deadline sanity check
        if deadline < date.today().isoformat():
            return "Deadline cannot be in the past."

        return Internship(
            internship_id=None,
            title=title,
            description=description,
            company_id=self._user_id,
            deadline=deadline
        )

    def view_apps(self, all_applications: list, all_internships: list):
        # getting all the ids for all internships posted by this company
        # an alternative here could be using a set instead of list for O(1) lookup
        my_internship_ids = [
            i._internship_id
            for i in all_internships
            if i._company_id == self._user_id
        ]

        return [a for a in all_applications if a._internship_id in my_internship_ids]

    def approve(self, application, notes=""):
        # an already approved application cannot be approved again!
        if application._status == "approved":
            return "Application already approved."

        # an already rejected application cannot be approved!
        if application._status == "rejected":
            return "Cannot approve rejected application."

        application._status = "approved"
        application._notes = notes

        return application

    def reject(self, application, notes=""):
        # an already rejected application cannot be rejected again!
        if application._status == "rejected":
            return "Application already rejected."

        # an already approved application cannot be rejected!
        if application._status == "approved":
            return "Cannot reject approved application."

        application._status = "rejected"
        application._notes = notes

        return application