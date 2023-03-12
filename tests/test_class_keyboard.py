import pytest

from shop.shop import Item


def test_get_attributes(keyboard):

    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'
    assert keyboard.pay_rate == 0.85
    assert len(Item.all) == 1


def test_change_language_attribute(keyboard):

    with pytest.raises(AttributeError):
        keyboard.language = 'CH'


def test_change_lang(keyboard):

    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'


def test_object_name_repr(keyboard):

    assert repr(keyboard) == 'KeyBoard(name=Dark Project KD87A, price=9600, quantity=5)'
