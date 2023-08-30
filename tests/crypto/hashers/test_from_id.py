import pytest
from cryptic.core.crypto import hashers


@pytest.mark.parametrize('_id, expected_type', [
    (hashers.ID.MD5, hashers.MD5),
    (hashers.ID.SHA256, hashers.SHA256),
    (hashers.ID.SHA512, hashers.SHA512),
])
def test_from_id(_id, expected_type):
    assert hashers.from_id(_id) is expected_type
