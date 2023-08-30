import enum
from Crypto.Hash import MD5 as md5


@enum.unique
class HasherId(enum.Enum):
    MD5 = "MD5"


class BaseHasher:

    def __init__(self, hasher_id: HasherId):
        self._hasher_id = hasher_id

    @property
    def id(self) -> HasherId:
        return self._hasher_id

    def hash(self, data: str) -> str:
        raise NotImplemented(f'Class is not implemented BaseHasher.hash')


class MD5(BaseHasher):

    def __init__(self):
        super().__init__(HasherId.MD5)

    def hash(self, data: str) -> str:
        return md5.new(data.encode('utf-8')).hexdigest()
