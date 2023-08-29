import re
from datetime import datetime


class BaseItem:
    ''' Base abstract class for all items '''

    def __init__(self, name: str):
        self._name = name
        self._modification_time = datetime.now()

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
    def modification_time(self):
        return self._modification_time

    def _update(self):
        self._modification_time = datetime.now()


class LoginItem(BaseItem):

    def __init__(self, name, login, password, email=''):
        super().__init__(name)
        self.login = login
        self.password = password
        self.email = email

    @property
    def login(self) -> str:
        return self._login
    
    @login.setter
    def login(self, new_login: str):
        if not isinstance(new_login, str):
            raise TypeError('The login attribute must be inherited from str')
        elif not new_login.strip():
            raise ValueError('Empty login is not allowed')

        self._login = new_login
        self._update()

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, new_password: str):
        if not isinstance(new_password, str):
            raise TypeError('The password attribute must be inherited from str')
        elif not new_password.strip():
            raise ValueError('Empty password is not allowed')
        
        self._password = new_password
        self._update()

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, new_email: str):
        if not isinstance(new_email, str):
            raise TypeError('The email attribute must be inherited from str')
        elif new_email and not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', new_email):
            raise ValueError(f'Invalid email address: {new_email}')
        
        self.email = new_email
        self._update()
