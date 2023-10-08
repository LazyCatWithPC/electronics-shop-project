"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_laptop():
    return Item('laptop', 25000, 4)


def test_calculate_total_price(item_laptop):
    assert item_laptop.calculate_total_price() == 100000


def test_apply_discount(item_laptop):
    item_laptop.pay_rate = 0.8
    item_laptop.apply_discount()
    assert item_laptop.price == 20000
