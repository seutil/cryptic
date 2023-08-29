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


def test_number():
    try:
        item = CardItem('Name', '1234 5678 9012 3456', '123')
    except Exception as e:
        pytest.fail(f'Exception raised: {e}')

    with pytest.raises(TypeError):
        item.number = 1234_5678_9012_3456

    with pytest.raises(ValueError):
        item.number = '2344'
    
    item.number = '1234 4324-4234 4321'
    assert item.number == '1234 4324-4234 4321'
