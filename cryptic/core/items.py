import re
from datetime import datetime


class BaseItem:
    ''' Base abstract class for all items '''

    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._modification_time = datetime.now()
        self._data = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if self._name == new_name:
            return

        self._name = new_name
        self._update()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        if self._description == new_description:
            return

        self._description = new_description
        self._update()

    @property
    def modification_time(self):
        return self._modification_time

    def data(self, key, new_value = None):
        if new_value is None:
            return self._data[key][0]
        elif not self._data[key][1](new_value):
            raise ValueError(f'Invalid "${key}" value: {new_value}')

        self._data[key][0] = new_value
        self._update()

    def _update(self):
        self._modification_time = datetime.now()


class LoginItem(BaseItem):

    def __init__(self, name, description):
        super().__init__(name, description)
        self._data = {
            'login': ['', self.__check_login],
            'email': ['', self.__check_email],
            'password': ['', self.__check_password],
            'notes': ['', self.__check_notes],
        }

    def __check_login(self, login: str):
        return login.strip() != ''
    
    def __check_email(self, email: str):
        return re.match(
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',
            email
        )

    def __check_password(self, password: str):
        return password.strip() != ''

    def __check_notes(self, notes: str):
        return True
