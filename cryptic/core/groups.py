import abc
from datetime import datetime
from . import items


class BaseGroup:
    """ Base class for all groups """

    def __init__(self, item_type: type[items.BaseItem], name: str, description=''):
        self._item_type = item_type
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

    @property
    def modification_time(self) -> datetime:
        return self._modification_time

    def append(self, item: items.BaseItem):
        if not self._check_item(item):
            return

        item._group = self
        self._items.append(item)
        self._update()

    def remove(self, item: items.BaseItem):
        if not isinstance(item, self._item_type):
            raise TypeError(f'Unexpected item type. Expected {self._item_type.name}, got {item.__class__.name}')

        self._items.remove(item)
        item._group = None
        self._update()

    def _update(self):
        self._modification_time = datetime.now()

    def _check_item(self, item: items.BaseItem) -> bool:
        if not isinstance(item, self._item_type):
            raise TypeError(f'Unexpected item type. Expected {self._item_type.name}, got {item.__class__.name}')
        elif item.group is not None:
            raise ValueError('Item group is already installed')
        elif item.group is self:
            return False

        for i in self._items:
            if i.name == item.name:
                raise ValueError('Item with specified name already exists')

        return True

    def __getitem__(self, key: int) -> items.BaseItem:
        return self._items[key]

    def __setitem__(self, key: int, item: items.BaseItem):
        if not self._check_item(item):
            return

        self._items[key]._group = None  # unset group for previous item
        item._group = self
        self._items[key] = item
        self._update()

    def __delitem__(self, key: int):
        self._items[key]._group = None
        del self._items[key]
        self._update()

    def __len__(self) -> int:
        return len(self._items)


class LoginsGroup(BaseGroup):

    def __init__(self, name: str, description=''):
        super().__init__(items.LoginItem, name, description)


class CardsGroup(BaseGroup):

    def __init__(self, name: str, description=''):
        super().__init__(items.CardItem, name, description)
