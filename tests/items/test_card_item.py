import pytest
from datetime import datetime
from cryptic.core.items import CardItem


@pytest.mark.parametrize('name, number, cvv, expiration, holder', [
    ('Name #1', '3742 4545 5400 1235', '221', datetime(2023, 11, 1), 'Holder A.V'),
    ('Name #2', '3742-4545-5400-1235', '2221', None, '')
])
def test_constructor_valid(name, number, cvv, expiration, holder):
    start = datetime.now()
    try:
        item = CardItem(name, number, cvv, expiration, holder)
    except Exception as e:
        pytest.fail(f'Exception raised: {e}')
    
    assert item.name == name
    assert item.number == number
    assert item.cvv == cvv
    assert item.expiration == expiration
    assert item.holder == holder
    assert start <= item.modification_time <= datetime.now()
