# This is an abstract base class
from abc import ABC
class User:
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password = password
    
    # currently assuming login logic is same for all kinds of users (Student, Company, Instructor)
    def login(self, email, password):
        return self.email == email and self.password == password