import pytest
from datetime import datetime
from cryptic.core.items import LoginItem


def test_constructor_valid():
    start = datetime.now()
    try:
        item = LoginItem('Login #1', 'login1', 'my-password')
    except Exception as e:
        pytest.fail(f'Exception raised: {e}')

    assert item.name == 'Login #1'
    assert item.login == 'login1'
    assert item.password == 'my-password'
    assert item.email == ''
    assert start <= item.modification_time <= datetime.now()
