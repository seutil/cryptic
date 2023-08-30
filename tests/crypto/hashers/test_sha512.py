from cryptic.core.crypto.hashers import SHA512, ID


def test_hash():
    hasher = SHA512()
    h = hasher.hash('hash-message')

    assert h == '282c5ba9729a6d08e112a4328d5f12a03a00ff08c55f2ec4c7895a54e71664eadd4b36cf3e9616c8c6529c968f7edd8f8d1e32dc9384b275ecf7f7b1b0776a49'
    assert len(h) == 128


def test_id():
    assert SHA512().id == ID.SHA512
