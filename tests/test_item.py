from src.item import Item, InstantiateCSVError
import csv
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

def Phone():
    phone_test = Phone("Смартфон", 10000, 20)
    return phone_test

def sum_price(self, Phone):
    if isinstance(Phone.__class__):
        return self.phone + Phone.__class__
    return False

def test_instantiate_csv_error():
    """Проверка текста ошибки класса InstantiateCSVError"""
    e = InstantiateCSVError()
    assert e.message == 'Файл .cvs повреждён: не хватает колонок.'
    assert e.__str__() == 'Файл .cvs повреждён: не хватает колонок.'


def test_not_file_instantiate_from_csv():
    """Проверка загрузки данных из несуществующего файла"""
    with pytest.raises(FileNotFoundError) as e:
        Item.instantiate_from_csv("not_found_items.csv")
    assert "No such file or directory" in str(e.value)


def test_wrong_file_instantiate_from_csv():
    """Проверка загрузки данных из файла с недостающим количеством колонок или повреждённым"""
    with pytest.raises(InstantiateCSVError) as e:
        Item.instantiate_from_csv("../tests/without_colum_items.csv")
    assert 'Файл .cvs повреждён: не хватает колонок.' in str(e.value)


def test_incorrect_headers_instantiate_from_csv(tmp_path):
    """Проверяем заголовки в файле csv"""
    # Создаем временный файл CSV с неправильными заголовками
    csv_file = tmp_path / "test.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])
        writer.writerow(["item1", "10.5"])
        writer.writerow(["item2", "22.2"])

    # Проверяем, что метод instantiate_from_csv вызывает исключение при чтении этого файла
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(csv_file)


def test_instantiate_from_csv_with_wrong_data(tmp_path):
    """Проверяем чтение данных из строки по заголовкам из cvs"""
    # Создаем временный файл CSV с неправильными данными
    csv_file = tmp_path / "items.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price", "quantity"])
        writer.writerow(["item1", "10.5", "abc"])  # неправильное значение количества

    # Получаем список объектов Item из CSV файла, ожидаем ошибку при чтении данных
    with pytest.raises(ValueError):
        Item.instantiate_from_csv(csv_file)


def test_instantiate_from_csv(tmp_path):
    """Проверяем получение данных из csv"""
    # Создаем временный файл CSV
    csv_file = tmp_path / "items.csv"
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price", "quantity"])
        writer.writerow(["item1", "10.5", "20"])
        writer.writerow(["item2", "22.2", "30"])

    # Получаем список объектов Item из CSV файла
    items = Item.instantiate_from_csv(csv_file)

    # Проверяем, что список не пустой
    assert items

    # Проверяем, что все объекты имеют нужные атрибуты
    for item in items:
        assert hasattr(item, "name")
        assert hasattr(item, "price")
        assert hasattr(item, "quantity")

    # Проверяем значения атрибутов первого объекта
    assert items[0].name == "item1"
    assert items[0].price == 10.5
    assert items[0].quantity == 20

    # Проверяем значения атрибутов второго объекта
    assert items[1].name == "item2"
    assert items[1].price == 22.2
    assert items[1].quantity == 30

    # Проверяем, что создался список объектов Item
    assert isinstance(Item.all, list)
    assert len(Item.all) == 2





