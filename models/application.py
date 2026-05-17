from datetime import date

class Application:
    def __init__(self, app_id, student_id, internship_id, status="pending", applied_at=None, notes=""):
        self._app_id = app_id
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

    def get_approved(self):
        return self._status == "approved"