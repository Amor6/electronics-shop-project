from src.phone import Phone
from src.item import Item
import pytest


class Phonet(Phone):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    #     self.name = name
    #     self.price = price
    #     self.quantity = quantity

    def __phonet(self, name, price, quantity):
        try:
            if not isinstance(name, str):
                raise TypeError("Название товара необходимо указано буквами")
            elif not isinstance(price, (int, float)):
                raise TypeError("Цену необходимо указать числом")
            elif not isinstance(quantity, int):
                raise TypeError("Количество необходимо указать целым числом")
            else:
                print(self)
        except TypeError as ER:
            print(ER)

