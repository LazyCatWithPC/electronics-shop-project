"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_laptop():
    return Item('laptop', 25000, 4)


def test_repr(item_laptop):
    assert repr(item_laptop) == "Item('laptop', 25000, 4)"


def test_str(item_laptop):
    assert str(item_laptop) == 'laptop'


def test_calculate_total_price(item_laptop):
    assert item_laptop.calculate_total_price() == 100000


def test_apply_discount(item_laptop):
    item_laptop.pay_rate = 0.8
    item_laptop.apply_discount()
    assert item_laptop.price == 20000


def test_name():
    item_laptop.name = "Office"
    assert item_laptop.name == "Office"


def test_string_to_number():
    assert Item.string_to_number('8.7') == 8
    assert Item.string_to_number('1') == 1


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    test_item = Item.all[1]
    assert test_item.price == 1000
    assert test_item.quantity == 3
