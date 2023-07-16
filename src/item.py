import csv
import os


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла CSV"""

    def __init__(self):
        self.message = 'Файл .cvs повреждён: не хватает колонок.'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, result_name) -> None:
        self.result_name = self.name[:0] + self.name[10:]

    def instantiate_from_csv(self):
        import csv
        with open('names.csv', newline='') as csvfile:
            self.name = csv.DictReader(csvfile)

    def string_to_number(self, name_string):
        self.name_string = str(self.name)

    def __repr__(self):
        return f'{self.__class__.__name__},({self.name}, {self.price},{self.quantity})'

    def __str__(self):
        return f'{self.name}, {self.price}'


def name():
    return None


@classmethod
def instantiate_from_csv(cls, path="../src/items.csv", reader=None, required_columns=None):
    """ Создание объектов из данных файла """
    items = []

    try:
        with open(os.path.abspath(path), 'r', newline='') as csvfile:
             # reader = csv.DictReader(csvfile, delimiter=',')
             # required_columns = ['name', 'price', 'quantity']
            if not all(column in reader.fieldnames for column in required_columns):
                raise InstantiateCSVError()

    except FileNotFoundError:
        print("Отсутствует файл .csv")
        raise

    except InstantiateCSVError as e:
        print(e)
        raise

    cls.all = items
    return cls.all
