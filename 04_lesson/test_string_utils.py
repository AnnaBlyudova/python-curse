import pytest
from string_utils import StringUtils

# позитивные тесты


@pytest.mark.parametrize('text, value', [
    ('skypro', 'Skypro'),
    ('Skypro', 'Skypro'),
    ('', ''),
    ('  ', '  '),
    ('123abc', '123abc'),
    ('a1b2c3', 'A1b2c3'),
    ('12345', '12345'),
    ('!@#$%', '!@#$%')
])
def test_capitalize_pos(text, value):
    utils = StringUtils()
    result = utils.capitalize(text)
    assert result == value


@pytest.mark.parametrize('text, symbol, expected', [
    ('Skypro', 'S', True),
    ('Skypro', 'C', False),
    ('', 'S', False),
    ('   ', 'p', False),
    ('SkyPro123', '1', True),
    ('SkyPro123', '5', False),
    ('!@#$%', '@', True),
    ('!@#$%', 'a', False)
])
def test_contains_pos(text, symbol, expected):
    utils = StringUtils()
    result = utils.contains(text, symbol)
    assert result == expected


@pytest.mark.parametrize('word, expected', [
    (' Skypro', 'Skypro'),
    ('Skypro', 'Skypro'),
    ('  Skypro', 'Skypro'),
    ('', ''),
    ('  ', ''),
    (' 123abc', '123abc'),
    (' !@#', '!@#'),
    ('  !@#', '!@#')
])
def test_trim_pos(word, expected):
    utils = StringUtils()
    result = utils.trim(word)
    assert result == expected


@pytest.mark.parametrize('word, symbol, expected', [
    ('Skypro', 'k', 'Sypro'),
    ('Skypro', 'x', 'Skypro'),
    ('', 'p', ''),
    ('  ', 'k', '  '),
    ('SkyPro123', '1', 'SkyPro23'),
    ('!@#$%', 'x', '!@#$%')
])
def test_delete_symbol_pos(word, symbol, expected):
    utils = StringUtils()
    result = utils.delete_symbol(word, symbol)
    assert result == expected

# негативные тесты


@pytest.mark.parametrize('input_data', [
    123,
    None,
    [1, 2, 3],
])
def test_capitalize_negative(input_data):
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.capitalize(input_data)


@pytest.mark.parametrize('input_data', [
    123,
    None,
    [1, 2, 3],
    True,
    3.14,
])
def test_trim_negative(input_data):
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.trim(input_data)


@pytest.mark.parametrize('input_data', [
    123,
    None,
    True,
    3.14,
])
def test_contains_negative(input_data):
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.contains(input_data, 'S')


@pytest.mark.parametrize('first, second', [
    (123, 'p'),
    (None, 'p'),
    (123, 456),
])
def test_delete_symbol_negative_first_wrong(first, second):
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.delete_symbol(first, second)


@pytest.mark.parametrize('first, second', [
    ('Skypro', 123),
    ('Skypro', None),
])
def test_delete_symbol_negative_second_wrong(first, second):
    utils = StringUtils()
    with pytest.raises(TypeError):
        utils.delete_symbol(first, second)
