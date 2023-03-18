import contextlib
import io
import os

import pytest

from shop.shop import Item


def test_get_attributes(item):

    assert item.name == 'товар 1'
    assert item.price == 10000
    assert item.quantity == 20
    assert item.pay_rate == 0.85
    assert len(Item.all) == 1


def test_change_attributes(item):

    item.name = 'товар 1_'
    item.price = 10
    item.quantity = 10
    item.pay_rate = 0.5

    assert item.name == 'товар 1_'
    assert item.price == 10
    assert item.quantity == 10
    assert item.pay_rate == 0.5


def test_calculate_total_price(item):

    assert item.calculate_total_price() == 200000


def test_apply_discount(item):

    item.pay_rate = 0.8
    assert item.apply_discount() == 8000
    assert item.price == 8000


def test_object_name_str(item):

    assert str(item) == 'товар 1'


def test_object_name_repr(item):

    assert repr(item) == 'Item(name=товар 1, price=10000, quantity=20)'


def test_exception_long_name(item):

    with pytest.raises(Exception):
        item.name = 'длина названия товара больше 10 символов'


def test_instantiate_from_csv():

    Item.instantiate_from_csv(path=os.path.join('tests', 'test.csv'))
    item_1 = Item.all[0]
    item_2 = Item.all[1]
    item_3 = Item.all[2]

    assert len(Item.all) == 3
    assert item_1.name == 'товар 1'
    assert item_1.price == 100
    assert item_1.quantity == 1
    assert item_2.name == 'товар 2'
    assert item_2.price == 55.5
    assert item_2.quantity == 3
    assert item_3.name == 'товар 3'
    assert item_3.price == 2000
    assert item_3.quantity == 6



def test_exception_file_damaged_1():

    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        Item.instantiate_from_csv(path=os.path.join('tests', 'bad_file_1.csv'))
    assert s.getvalue() == 'InstantiateCSVError: Файл item.csv поврежден\n'


def test_exception_file_damaged_2():

    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        Item.instantiate_from_csv(path=os.path.join('tests', 'bad_file_2.csv'))
    assert s.getvalue() == 'InstantiateCSVError: Файл item.csv поврежден\n'


def test_attributes_price_and_quantity():

    with pytest.raises(AttributeError):
        Item(name='товар 1', price=-10000, quantity=-1)


def test_add(item):

    assert item + item == 40


def test_add_exception(item):

    with pytest.raises(TypeError):
        result = item + 10

def test_exception_file_not_found():
    s = io.StringIO()
    with contextlib.redirect_stdout(s):
        Item.instantiate_from_csv(path=os.path.join('tests', 'file.csv'))
    assert s.getvalue() == f'FileNotFoundError: Отсутствует файл {os.path.join("tests", "file.csv")}\n'
