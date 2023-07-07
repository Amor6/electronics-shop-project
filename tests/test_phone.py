from src.phone import Phone
from src.item import Item
from src.item import name
import pytest

def Phone():
    phone_test = Phone("Смартфон", 10000, 20)
    return phone_test

def sum_price(self, Phone):
    if isinstance(Phone.__class__):
        return self.phone + Phone.__class__
    return False


