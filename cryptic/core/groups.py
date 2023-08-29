from datetime import datetime


class BaseGroup:
    ''' Base class for all groups '''

    def __init__(self, name: str, description=''):
        self._name = name
        self._description = description
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
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, new_description: str):
         if self._description == new_description:
             return
         
         self._description = new_description
         self._update()

    def _update(self):
        self._modification_time = datetime.now()
