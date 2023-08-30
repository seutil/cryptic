import enum
import base64
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


@enum.unique
class ID(enum.Enum):
    AES_CBC = "AES-CBC"


class BaseCipher:

    def __init__(self, _id: ID, key: str, salt: str):
        self._id = _id
        self.key = key
        self.salt = salt

    @property
    def id(self) -> ID:
        return self._id

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, new_key: str):
        if not new_key:
            raise ValueError('Empty encryption key is not allowed')

        self._key = new_key

    @property
    def salt(self) -> str:
        return self._salt

    @salt.setter
    def salt(self, new_salt: str):
        if not new_salt:
            raise ValueError('Empty salt is not allowed')

        self._salt = new_salt

    def encrypt(self, data: str) -> str:
        raise NotImplemented('Class is not implemented BaseCipher.encrypt')

    def decrypt(self, data: str) -> str:
        raise NotImplemented('Class is not implemented BaseCipher.decrypt')


class BaseAES(BaseCipher):

    def __init__(self, mode, _id: ID, key: str, salt: str):
        super().__init__(_id, key, salt)
        self._mode = mode

    def encrypt(self, data: str) -> str:
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self._pbkdf2(), self._mode, iv)
        encrypted = iv + cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt(self, data: str) -> str:
        decoded = base64.b64decode(data.encode())
        cipher = AES.new(self._pbkdf2(), self._mode, decoded[:AES.block_size])
        decrypted = unpad(cipher.decrypt(decoded[AES.block_size:]), AES.block_size)
        return decrypted.decode('utf-8')

    def _pbkdf2(self) -> bytes:
        return PBKDF2(self._key, self._salt.encode(), count=4096, hmac_hash_module=SHA256)


class AES_CBC(BaseAES):

    def __init__(self, key: str, salt: str):
        super().__init__(AES.MODE_CBC, ID.AES_CBC, key, salt)
