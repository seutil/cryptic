import re
from datetime import datetime


class BaseItem:
    ''' Base class for all items '''

    def __init__(self, name: str):
        self._name = name
        self._modification_time = datetime.now()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        if self._name == new_name:
            return

        self._name = new_name
        self._update()

    @property
    def modification_time(self) -> datetime:
        return self._modification_time

    def _update(self):
        self._modification_time = datetime.now()


class LoginItem(BaseItem):

    def __init__(self, name: str, login: str, password: str, email=''):
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
        
        self._email = new_email
        self._update()


class CardItem(BaseItem):

    def __init__(
            self, name: str, number: str, cvv: str,
            expiration=None, holder=''):
        super().__init__(name)
        self.number = number
        self.cvv = cvv
        self.expiration = expiration
        self.holder = holder

    @property
    def number(self) -> str:
        return self._number
    
    @number.setter
    def number(self, new_number: str):
        if not isinstance(new_number, str):
            raise TypeError('The number attribute must be inherited from str')
        elif not re.match(r'(\d{4})(-?)(\d{4})(\2\d{4}){2}', new_number):
            raise ValueError(f'Invalid card number: {new_number}')
        
        self._number = new_number
        self._update()
    
    @property
    def cvv(self) -> str:
        return self._cvv
    
    @cvv.setter
    def cvv(self, new_cvv: str):
        if not isinstance(new_cvv, str):
            raise TypeError('The cvv attribute must be inherited from str')
        elif not re.match(r'\d{3,4}', new_cvv):
            raise ValueError(f'Invalid card cvv: {new_cvv}')
        
        self._cvv = new_cvv
        self._update()

    @property
    def expiration(self) -> datetime:
        return self._expiration

    @expiration.setter
    def expiration(self, new_expiration: datetime | None):
        if not isinstance(new_expiration, datetime | None):
            raise TypeError('The card expiration date must be inherited from datetime')
        
        self._expiration = new_expiration
        self._update()

    @property
    def holder(self) -> str:
        return self._holder
    
    @holder.setter
    def holder(self, new_holder: str):
        if not isinstance(new_holder, str):
            raise TypeError('The card holder must be inherited from str')

        self._holder = new_holder
        self._update()
