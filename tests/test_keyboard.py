import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    test_kb = Keyboard('Kb 1A', 500, 3)
    return test_kb


def test_init(keyboard):
    assert keyboard.name == 'Kb 1A'
    assert keyboard.price == 500
    assert keyboard.quantity == 3


def test_change_lang(keyboard):
    assert str(keyboard.language) == "EN"
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang()
    assert str(keyboard.language) == "EN"
