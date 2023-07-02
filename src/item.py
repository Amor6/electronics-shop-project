
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
