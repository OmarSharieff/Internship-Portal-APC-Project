from datetime import date


class Application:
    _id_counter = 1

    def __init__(self, student_id, internship_id,
                 status="pending", applied_at=None, notes=""):

        self._app_id = Application._id_counter
        Application._id_counter += 1

        self._student_id = student_id
        self._internship_id = internship_id
        self._status = status
        self._applied_at = applied_at if applied_at else date.today().isoformat()
        self._notes = notes

    def update_status(self, new_status):
        allowed = ["pending", "under_review", "approved", "rejected"]

        if new_status not in allowed:
            return "Invalid status."

        if self._status == new_status:
            return f"Application is already {new_status}."

        self._status = new_status
        return f"Status updated to {new_status}."

    def add_notes(self, notes):
        self._notes = notes

    def get_status(self):
        return self._status

    def get_student_id(self):
        return self._student_id

    def get_internship_id(self):
        return self._internship_id

    def get_approved(self):
        return self._status == "approved"

    def __str__(self):
        return f"Application({self._app_id}, {self._status})"