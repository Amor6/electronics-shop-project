class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        print(Item.all)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        Item.pay_rate = 0.8
        print(Item.pay_rate)

    def __repr__(self):
        return f'Item{self.name}, {self.price},{self.quantity}'

    def __str__(self):
        return f'{self.name}'
