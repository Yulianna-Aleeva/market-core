from src.classes.category import Category
from src.classes.category_iterator import CategoryIterator


def test_category_iterator(first_category: Category, category_data: list[dict]) -> None:
    """Проверка работы итератора по товарам категории."""
    iterator = CategoryIterator(first_category)
    products_from_iterator = list(iterator)

    expected_products_data = category_data[0]["products"]

    assert len(products_from_iterator) == len(expected_products_data)

    for index, product in enumerate(products_from_iterator):
        assert product.name == expected_products_data[index]["name"]
        assert product.price == expected_products_data[index]["price"]
