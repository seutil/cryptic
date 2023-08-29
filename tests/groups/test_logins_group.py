import pytest
from datetime import datetime
from cryptic.core.items import LoginItem, CardItem
from cryptic.core.groups import LoginsGroup


def test_constructor():
    group = LoginsGroup('Group', 'Description')

    assert group.name == 'Group'
    assert group.description == 'Description'
    assert len(group) == 0


def test_name():
    before_init = datetime.now()
    group = LoginsGroup('Group')
    end_init = datetime.now()
    assert before_init <= group.modification_time <= end_init
    assert group.name == 'Group'

    before_update1 = datetime.now()
    group.name = 'New name'
    end_update1 = datetime.now()
    assert before_update1 <= group.modification_time <= end_update1
    assert group.name == 'New name'

    group.name = 'New name'  # "don't" change group name
    assert before_update1 <= group.modification_time <= end_update1
    assert group.name == 'New name'


def test_description():
    before_init = datetime.now()
    group = LoginsGroup('Name', 'Description')
    end_init = datetime.now()
    assert before_init <= group.modification_time <= end_init
    assert group.description == 'Description'

    before_update1 = datetime.now()
    group.description = 'New description'
    end_update1 = datetime.now()
    assert before_update1 <= group.modification_time <= end_update1
    assert group.description == 'New description'

    group.description = 'New description'  # "don't" change group description
    assert before_update1 <= group.modification_time <= end_update1


def test_append():
    group = LoginsGroup('Name', 'Description')
    assert len(group) == 0

    item = LoginItem('Item 1', 'Login', 'Password')
    before_update = datetime.now()
    group.append(item)
    assert before_update <= group.modification_time <= datetime.now()

    with pytest.raises(ValueError):
        group.append(LoginItem('Item 1', 'Login', 'Password'))

    with pytest.raises(TypeError):
        group.append(CardItem('', '1111 2222 3333 4444', '123'))

    assert len(group) == 1
    assert item.group is group


def test_remove():
    group = LoginsGroup('Name')
    item = LoginItem('Item #1', 'login', 'password')

    group.append(item)
    with pytest.raises(TypeError):
        group.remove(CardItem('Item #1', '1111 2222 3333 4444', '123'))

    with pytest.raises(ValueError):
        group.remove(LoginItem('Item #2', 'login', 'password'))

    before_update = datetime.now()
    group.remove(item)
    assert before_update <= group.modification_time <= datetime.now()
    assert len(group) == 0
    assert item.group is None


def test_getitem():
    group = LoginsGroup('Logins Group')
    item1 = LoginItem('Item #1', 'login', 'password')
    item2 = LoginItem('Item #2', 'login', 'password')

    group.append(item1)
    group.append(item2)

    assert group[0] == item1
    assert group[1] == item2


def test_setitem():
    group = LoginsGroup('Logins Group')
    item1 = LoginItem('Item #1', 'login', 'password')
    item2 = LoginItem('Item #2', 'login', 'password')
    item3 = LoginItem('Item #3', 'login', 'password')
    item4 = LoginItem('Item #4', 'login', 'password')

    group.append(item1)
    group.append(item2)
    before_update1 = datetime.now()
    group[0] = item3
    assert before_update1 <= group.modification_time <= datetime.now()
    before_update2 = datetime.now()
    group[1] = item4
    assert before_update2 <= group.modification_time <= datetime.now()

    assert item1.group is None
    assert item2.group is None
    assert item3.group is group
    assert item4.group is group


def test_delitem():
    group = LoginsGroup('Logins Group')
    item1 = LoginItem('Item #1', 'login', 'password')
    item2 = LoginItem('Item #2', 'login', 'password')
    item3 = LoginItem('Item #3', 'login', 'password')
    item4 = LoginItem('Item #4', 'login', 'password')

    group.append(item1)
    group.append(item2)
    group.append(item3)
    group.append(item4)
    del group[0]
    del group[0]

    assert len(group) == 2
    assert item1.group is None
    assert item2.group is None


def test_len():
    group = LoginsGroup('Logins Group')
    assert len(group) == 0
    item1 = LoginItem('Item #1', 'login', 'password')
    item2 = LoginItem('Item #2', 'login', 'password')
    item3 = LoginItem('Item #3', 'login', 'password')
    item4 = LoginItem('Item #4', 'login', 'password')

    group.append(item1)
    group.append(item2)
    group.append(item3)
    group.append(item4)
    group.remove(item3)
    del group[0]

    assert len(group) == 2
