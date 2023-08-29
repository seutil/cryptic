import pytest
from datetime import datetime
from cryptic.core.items import LoginItem


@pytest.mark.parametrize('name, login, password, email', [
    ('', 'insideewquick-witted', 'DF3n4nYXk8jK', 'benjaminmiller@email.com'),
    ('name', 'psstwhereasfan', 'D42y9N9VMtpg', 'rachelmoore77@email.com'),
])
def test_constructor_valid(name, login, password, email):
    start = datetime.now()
    try:
        item = LoginItem(name, login, password, email)
    except Exception as e:
        pytest.fail(f'Exception raised: {e}')

    assert item.name == name
    assert item.login == login
    assert item.password == password
    assert item.email == email
    assert start <= item.modification_time <= datetime.now()


def test_login():
    item = LoginItem('', 'login', 'password')
    with pytest.raises(TypeError):
        item.login = 123
    
    with pytest.raises(ValueError):
        item.login = ''
    
    try:
        item.login = 'login'
    except Exception as e:
        pytest.fail('Exception raised: {e}')
