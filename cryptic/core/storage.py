import enum
from . import groups, exceptions
from .crypto import hashers, ciphers


class Storage:

    @enum.unique
    class Status(enum.Enum):
        CLOSED = 1
        OPENED = 2
        MODIFIED = 3

    def __init__(
            self, name: str, password: str, hasher: hashers.BaseHasher,
            cipher: ciphers.BaseCipher, description=''):
        self._location = ''
        self._name = name
        self._password = password
        self._hasher = hasher
        self._cipher = cipher
        self._description = description
        self._groups: list[groups.BaseGroup] = []
        self._closed_state = self._ClosedState(self)
        self._opened_state = self._OpenedState(self)
        self._modified_state = self._ModifiedState(self)
        self._state = self._opened_state

    @property
    def location(self) -> str:
        return self._location

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._state.set_name(new_name)

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, new_description: str):
        self._state.set_description(new_description)

    @property
    def password(self) -> str:
        return self._state.password

    @password.setter
    def password(self, new_password: str):
        self._state.password = new_password

    @property
    def hasher(self) -> hashers.BaseHasher:
        return self._state.hasher

    @hasher.setter
    def hasher(self, new_hasher: hashers.BaseHasher):
        self._state.hasher = new_hasher

    @property
    def cipher(self):
        return self._state.cipher

    @cipher.setter
    def cipher(self, new_cipher: ciphers.BaseCipher):
        self._state.cipher = new_cipher

    @property
    def status(self) -> Status:
        return self._state.status

    def close(self):
        self._state = self._closed_state

    def open(self, password: str):
        self._state.open(password)

    def append(self, group: groups.BaseGroup):
        self._state.append(group)

    def remove(self, group: groups.BaseGroup):
        self._state.remove(group)

    def __getitem__(self, key):
        return self._state[key]

    def __setitem__(self, key, group: groups.BaseGroup):
        self._state[key] = group

    def __len__(self):
        return len(self._state)

    class _ClosedState:

        def __init__(self, storage):
            self._storage = storage

        def set_name(self, new_name: str):
            raise exceptions.StorageClosedError(self._storage)

        def set_description(self, new_description: str):
            raise exceptions.StorageClosedError(self._storage)

        @property
        def password(self) -> str:
            raise exceptions.StorageClosedError(self._storage)

        @password.setter
        def password(self, new_password: str):
            raise exceptions.StorageClosedError(self._storage)

        @property
        def hasher(self) -> hashers.BaseHasher:
            raise exceptions.StorageClosedError(self._storage)

        @hasher.setter
        def hasher(self, new_hasher: hashers.BaseHasher):
            raise exceptions.StorageClosedError(self._storage)

        @property
        def cipher(self) -> ciphers.BaseCipher:
            raise exceptions.StorageClosedError(self._storage)

        @cipher.setter
        def cipher(self, new_cipher: ciphers.BaseCipher):
            raise exceptions.StorageClosedError(self._storage)

        @property
        def status(self):
            return Storage.Status.CLOSED

        def open(self, password: str):
            if self._storage._password != password:
                raise ValueError('Invalid password')

            self._storage._state = self._storage._opened_state

        def append(self, group: groups.BaseGroup):
            raise exceptions.StorageClosedError(self._storage)

        def remove(self, group: groups.BaseGroup):
            raise exceptions.StorageClosedError(self._storage)

        def __getitem__(self, key):
            raise exceptions.StorageClosedError(self._storage)

        def __setitem__(self, key, group: groups.BaseGroup):
            raise exceptions.StorageClosedError(self._storage)

        def __len__(self):
            raise exceptions.StorageClosedError(self._storage)

    class _OpenedState:

        def __init__(self, storage):
            self._storage = storage

        def set_name(self, new_name: str):
            self._storage._name = new_name
            self._storage._state = self._storage._modified_state

        def set_description(self, new_description: str):
            self._storage._description = new_description
            self._storage._state = self._storage._modified_state

        @property
        def password(self) -> str:
            return self._storage._password

        @password.setter
        def password(self, new_password: str):
            self._storage._password = new_password
            self._storage._state = self._storage._modified_state

        @property
        def hasher(self) -> hashers.BaseHasher:
            return self._storage._hasher

        @hasher.setter
        def hasher(self, new_hasher: hashers.BaseHasher):
            self._storage._hasher = new_hasher
            self._storage._state = self._storage._modified_state

        @property
        def cipher(self) -> ciphers.BaseCipher:
            return self._storage._cipher

        @cipher.setter
        def cipher(self, new_cipher: ciphers.BaseCipher):
            self._storage.cipher = new_cipher
            self._storage._state = self._storage._modified_state

        @property
        def status(self):
            return Storage.Status.OPENED

        def open(self, password: str):
            ...

        def append(self, group: groups.BaseGroup):
            if not self._check_new_group(group):
                return

            self._storage._state = self._storage._modified_state
            self._storage.append(group)

        def remove(self, group: groups.BaseGroup):
            self._storage._state = self._storage._modified_state
            self._storage.remove(group)

        def _check_new_group(self, group: groups.BaseGroup) -> bool:
            if group.storage is self._storage:
                return False
            elif group.storage is not None:
                raise ValueError("Group's storage is already installed")

            for g in self._storage._groups:
                if g.name == group.name:
                    raise ValueError('Group with same name already contains in storage')

            return True

        def __getitem__(self, key: int):
            return self._storage._groups[key]

        def __setitem__(self, key: int, group: groups.BaseGroup):
            if not self._check_new_group(group):
                return

            self._storage[key]._storage = None  # unset previous group storage
            group._storage = self._storage
            self._storage[key] = group
            self._storage._state = self._storage._modified_state

        def __delitem__(self, key: int):
            self._storage._groups[key]._storage = None
            del self._storage._groups[key]
            self._storage._state = self._storage._modified_state

        def __len__(self):
            return len(self._storage._groups)

    class _ModifiedState(_OpenedState):

        def status(self):
            return Storage.Status.MODIFIED
