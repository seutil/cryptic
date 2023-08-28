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
