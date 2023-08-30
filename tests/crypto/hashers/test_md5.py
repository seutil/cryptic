from cryptic.core.crypto.hashers import MD5, HasherId


def test_hash():
    hasher = MD5()
    h = hasher.hash('hash-message')

    assert len(h) == 32
    assert h == '7ed86252985e35db3e98e423f356d167'


def test_id():
    assert MD5().id == HasherId.MD5
