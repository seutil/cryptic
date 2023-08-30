import pytest
from cryptic.core.crypto import ciphers


@pytest.mark.parametrize('data, key, salt', [
    ('rg4evpAlNk', 'MrQgccPorz', 'UsApwgjMcz'),
])
def test_cipher_cycle(data, key, salt):
    cipher = ciphers.AES_CBC(key, salt)
    assert data == cipher.decrypt(cipher.encrypt(data))


def test_id():
    assert ciphers.AES_CBC('12', '12').id == ciphers.CipherId.AES_CBC
