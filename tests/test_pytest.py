import pytest
from main import check_auth


@pytest.mark.parametrize(
    'log,pas,expected',
    (
            ['admin', 'password', 'Добро пожаловать'],
            ['123', 'password', 'Доступ ограничен'],
            ['admin', '123', 'Доступ ограничен'],
            ['qwr', '123', 'Доступ ограничен'],
    )
)
def test_check_auth(log, pas, expected):
    actual = check_auth(log, pas)
    assert actual == expected
