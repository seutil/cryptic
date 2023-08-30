from cryptic.core.crypto.hashers import SHA256, ID


def test_hash():
    hasher = SHA256()
    h = hasher.hash('hash-message')

    assert h == '511f3f1228c1e4971f79f66b6976760b84b81b156802c5fe64bd83dff676936c'
    assert len(h) == 64


def test_id():
    assert SHA256().id == ID.SHA256
