from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id
        self._name = name
        self._email = email.lower()
        self._password = password

    def login(self, email, password):
        return self._email == email.lower() and self._password == password

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    @abstractmethod
    def __str__(self):
        pass