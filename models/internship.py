
class Internship:
    def __init__(self, internship_id, title, description, company_id, deadline, is_open=True):
        self._internship_id = internship_id
        self._title = title
        self._description = description
        self._company_id = company_id
        self._deadline = deadline
        self._is_open = is_open

    def get_details(self):
        return {"internship_id": self._internship_id,
            "title": self._title,
            "description": self._description,
            "company_id": self._company_id,
            "deadline": self._deadline,
            "is_open": self._is_open
        }
    
    def close(self):
        if not self._is_open:
            return "Internship is already closed!"
        self._is_open = False
        return "Internship closed successfully"