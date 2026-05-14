class Internship:
    _id_counter = 1

    def __init__(self, title, description,
                 company_id, deadline, is_open=True):

        self._internship_id = Internship._id_counter
        Internship._id_counter += 1

        self._title = title
        self._description = description
        self._company_id = company_id
        self._deadline = deadline
        self._is_open = is_open

    def get_details(self):
        return {
            "internship_id": self._internship_id,
            "title": self._title,
            "description": self._description,
            "company_id": self._company_id,
            "deadline": self._deadline,
            "is_open": self._is_open
        }

    def get_id(self):
        return self._internship_id

    def get_company_id(self):
        return self._company_id

    def is_open(self):
        return self._is_open

    def get_deadline(self):
        return self._deadline

    def close(self):
        if not self._is_open:
            return "Internship is already closed!"

        self._is_open = False
        return "Internship closed successfully"

    def __str__(self):
        return f"Internship({self._title})"