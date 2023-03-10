import pytest

from shop.shop import Item, Phone


def test_get_attributes(phone):

    assert phone.name == 'iPhone 14'
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2
    assert phone.pay_rate == 0.85
    assert len(Item.all) == 1


def test_change_number_of_sim_correct_data(phone):

    phone.number_of_sim = 1

    assert phone.number_of_sim == 1


def test_change_number_of_sim_incorrect_data(phone):

    with pytest.raises(ValueError):
        phone.number_of_sim = 3


def test_attribute_number_of_sim():

    with pytest.raises(AttributeError):
        Phone(name='iPhone 10', price=60000, quantity=50, number_of_sim=4)


def test_add(item, phone):

    assert item + phone == 25
    assert phone + item == 25
    assert phone + phone == 10


def test_add_exception(phone):

    with pytest.raises(TypeError):
        result = phone + 10


def test_object_name_repr(phone):

    assert repr(phone) == 'Phone(name=iPhone 14, price=120000, quantity=5, number_of_sim=2)'