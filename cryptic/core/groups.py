import abc
import items
from datetime import datetime


class BaseGroup:
    ''' Base class for all groups '''

    def __init__(self, name: str, description=''):
        self._name = name
        self._description = description
        self._modification_time = datetime.now()
        self._items = []

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

    @abc.abstractmethod
    def _check_item(self, item: items.BaseItem):
        raise NotImplementedError(f'Class "{self.__class__.name}" is not implemented')

    def __getitem__(self, key: int) -> items.BaseItem:
        return self._items[key]

    def __setitem__(self, key: int, value: items.BaseItem):
        self._check_item(value)
        # TODO: check that item's group
        # TODO: chat that item is not in the list
        self._items[key] = value
        self._update()

    def __delitem__(self, key: int):
        # TODO: set item group to None
        del self._items[key]
        self._update()

    def __len__(self) -> int:
        return len(self._items)
