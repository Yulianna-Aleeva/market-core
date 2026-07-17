from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json


def test_read_json(loaded_data, mock_json_data):
    assert len(loaded_data) == 2
    assert loaded_data[0]["name"] == "Смартфоны"
    assert loaded_data[1]["name"] == "Телевизоры"
    assert len(loaded_data[0]["products"]) == 1
    assert loaded_data[0]["products"][0]["price"] == 180000.0


def test_create_objects_from_json(loaded_data):
    categories = create_objects_from_json(loaded_data)
    assert len(categories) == 2
    assert isinstance(categories[0], Category)
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].name == "Смартфоны"
    assert categories[0].products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[0].products[0].quantity == 5
    assert categories[0].product_count == 12
    assert categories[1].name == "Телевизоры"
    assert categories[1].products[0].name == '55" QLED 4K'
    assert categories[1].product_count == 12
    assert Category.category_count == 2
    assert Category.product_count == 12
