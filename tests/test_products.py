from src.product import Product


def test_product_init(first_product: Product, second_product: Product, category_data: list[dict]) -> None:
    """Корректная инициализация объектов Product."""
    first_data = category_data[0]["products"][0]  # Смартфон
    second_data = category_data[1]["products"][0]  # Телевизор

    assert first_product.name == first_data["name"]
    assert second_product.description == second_data["description"]
    assert first_product.price == first_data["price"]
    assert second_product.quantity == second_data["quantity"]


def test_product_init_edge_cases() -> None:
    """Пустые строки, нулевые цена и количество."""
    product = Product("", "", 0.0, 0)
    assert product.name == ""
    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0


def test_product_init_negative_values() -> None:
    """Отрицательные значения."""
    product = Product("Товар", "Описание", -500.0, -10)
    assert product.price == -500.0
    assert product.quantity == -10
