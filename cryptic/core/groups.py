import abc
import items
from datetime import datetime


class BaseGroup:
    ''' Base class for all groups '''

    def __init__(self, name: str, description=''):
        self._name = name
        self._description = description
        self._modification_time = datetime.now()
        self._items: list[items.BaseItem] = []

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

    def __setitem__(self, key: int, item: items.BaseItem):
        self._check_item(item)
        if item.group is not None:
            raise ValueError('Item group is already installed')
        elif item in self._items:
            return

        self._items[key] = item
        self._update()

    def __delitem__(self, key: int):
        self._items[key]._group = None
        del self._items[key]
        self._update()

    def __len__(self) -> int:
        return len(self._items)


class LoginsGroup(BaseGroup):

    def _check_item(self, item: items.BaseItem):
        return isinstance(item, items.LoginItem)


class CardsGroup(BaseGroup):

    def _check_item(self, item: items.BaseItem):
        return isinstance(item, items.CardItem)
