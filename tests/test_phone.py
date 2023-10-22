import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def test_phone():
    return Phone('iPhone', 20000, 5, 2)


@pytest.fixture
def test_item():
    return Item('Телефон', 15000, 2)


def test_init(test_phone):
    assert test_phone.name == 'iPhone'
    assert test_phone.price == 20000
    assert test_phone.quantity == 5
    assert test_phone.number_of_sim == 2


def test_repr(test_phone):
    assert repr(test_phone) == "Phone('iPhone', 20000, 5, 2)"


def test_add_phone_and_item(test_item, test_phone):
    quantity = test_phone + test_item
    assert quantity == (test_phone.quantity + test_item.quantity)


def test_add_item_and_phone(test_item, test_phone):
    quantity = test_item + test_phone
    assert quantity == (test_item.quantity + test_phone.quantity)
