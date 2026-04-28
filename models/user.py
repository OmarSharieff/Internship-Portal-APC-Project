# This is an abstract base class
from abc import ABC
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
    
    # currently assuming login logic is same for all kinds of users (Student, Company, Instructor)
    def login(self, email, password):
        return self.email == email and self.password == password