import enum
from Crypto.Hash import MD5 as md5, SHA256 as s256, SHA512 as s512


@enum.unique
class HasherId(enum.Enum):
    MD5 = "MD5"
    SHA256 = "SHA256"
    SHA512 = "SHA512"


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


class SHA256(BaseHasher):

    def __init__(self):
        super().__init__(HasherId.SHA256)

    def hash(self, data: str) -> str:
        return s256.new(data.encode('utf-8')).hexdigest()


class SHA512(BaseHasher):

    def __init__(self):
        super().__init__(HasherId.SHA512)

    def hash(self, data: str) -> str:
        return s512.new(data.encode('utf-8')).hexdigest()


def from_id(_id: HasherId) -> type[BaseHasher]:
    return {
        HasherId.MD5: MD5,
        HasherId.SHA256: SHA256,
        HasherId.SHA512: SHA512
    }[_id]
