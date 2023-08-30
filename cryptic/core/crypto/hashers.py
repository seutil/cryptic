import enum
from Crypto.Hash import MD5 as md5, SHA256 as s256, SHA512 as s512


@enum.unique
class ID(enum.Enum):
    MD5 = "MD5"
    SHA256 = "SHA256"
    SHA512 = "SHA512"


class BaseHasher:

    def __init__(self, _id: ID):
        self._id = _id

    @property
    def id(self) -> ID:
        return self._id

    def hash(self, data: str) -> str:
        raise NotImplemented(f'Class is not implemented BaseHasher.hash')


class MD5(BaseHasher):

    def __init__(self):
        super().__init__(ID.MD5)

    def hash(self, data: str) -> str:
        return md5.new(data.encode('utf-8')).hexdigest()


class SHA256(BaseHasher):

    def __init__(self):
        super().__init__(ID.SHA256)

    def hash(self, data: str) -> str:
        return s256.new(data.encode('utf-8')).hexdigest()


class SHA512(BaseHasher):

    def __init__(self):
        super().__init__(ID.SHA512)

    def hash(self, data: str) -> str:
        return s512.new(data.encode('utf-8')).hexdigest()


def from_id(_id: ID) -> type[BaseHasher]:
    return {
        ID.MD5: MD5,
        ID.SHA256: SHA256,
        ID.SHA512: SHA512
    }[_id]
