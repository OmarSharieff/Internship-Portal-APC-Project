from datetime import date
from models.user import User
from models.internship import Internship


class Company(User):
    def __init__(self, user_id, name,
                 email, password, industry, location):

        super().__init__(user_id, name, email, password)

        self._industry = industry
        self._location = location

    def post_intern(self, title, description,
                    deadline, all_internships):

        if title.strip() == "":
            return "Title cannot be empty."

        duplicate = [
            i for i in all_internships
            if i._company_id == self._user_id and i._title == title
        ]

        if len(duplicate) > 0:
            return "Internship with this title already exists."

        if deadline < date.today().isoformat():
            return "Deadline cannot be in the past."

        return Internship(
            title=title,
            description=description,
            company_id=self._user_id,
            deadline=deadline
        )

    def view_apps(self, all_applications, all_internships):

        my_internship_ids = [
            i.get_id()
            for i in all_internships
            if i.get_company_id() == self._user_id
        ]

        return [
            a for a in all_applications
            if a.get_internship_id() in my_internship_ids
        ]

    def approve(self, application, notes=""):

        if application.get_status() == "approved":
            return "Application already approved"

        if application.get_status() == "rejected":
            return "Cannot approve rejected application"

        application.update_status("approved")
        application.add_notes(notes)

        return application

    def reject(self, application, notes=""):

        if application.get_status() == "rejected":
            return "Application already rejected"

        if application.get_status() == "approved":
            return "Cannot reject approved application"

        application.update_status("rejected")
        application.add_notes(notes)

        return application

    def __str__(self):
        return f"Company({self._name})"