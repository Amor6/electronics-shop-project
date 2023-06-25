from src.item import Item
import pytest


@pytest.fixture
def item():
    item_test = Item("Смартфон", 10000, 20)
    return item_test

def test_name():
    item.name = "Ноутбук"
    assert item.name == "Ноутбук"



def test_price():
    item.price = 2000
    assert item.price == 2000
    item.price = 200.0
    assert item.price == 200.0

def test_quantity():
    item.quantity = 20
    assert item.quantity == 20

def test_repr():
    __repr__ = "Смартфон"
    assert __repr__ == "Смартфон"

def test_str():
    __str__ = 5000
    assert __str__ == 5000












