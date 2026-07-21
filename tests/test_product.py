import pytest

from src.classes.product import Product


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


def test_product_private_price(first_product: Product) -> None:
    """Проверка недоступности прямого доступа к __price."""
    with pytest.raises(AttributeError):
        _ = first_product.__price  # noqa


def test_product_getter_setter_positive(first_product: Product) -> None:
    """Геттер возвращает текущее значение, сеттер корректно меняет цену."""
    old_price = first_product.price
    new_price = old_price + 100.0
    first_product.price = new_price
    assert first_product.price == new_price


def test_product_setter_negative_or_zero(first_product: Product) -> None:
    """Сеттер не изменяет цену при отрицательных или нулевых значениях."""
    price_before = first_product.price
    for value in (-500.0, -10.0, 0.0):
        first_product.price = value
        assert first_product.price == price_before


def test_product_new_product(first_product: Product) -> None:
    """Класс-метод new_product создает корректный экземпляр."""
    # Создаем новый продукт из словаря с данными первого продукта
    created = Product.new_product(
        dict(
            name=first_product.name,
            description=first_product.description,
            price=first_product.price,
            quantity=first_product.quantity,
        )
    )

    # Проверяем сразу все атрибуты
    for attr in ["name", "description", "price", "quantity"]:
        assert getattr(created, attr) == getattr(first_product, attr), f"Ошибка в поле {attr}"


def test_product_str(first_product: Product) -> None:
    """Возвращает строку с данными продукта."""
    assert str(first_product) == (
        f"{first_product.name}, {first_product.price} руб. Остаток: {first_product.quantity} шт."
    )


def test_product_add(first_product: Product, second_product: Product) -> None:
    """Возвращает суммарную стоимость товаров двух продуктов."""
    expected = first_product.price * first_product.quantity + second_product.price * second_product.quantity
    assert first_product + second_product == expected


def test_product_add_type_error(first_product: Product) -> None:
    """Проверка ошибки при сложении продукта с числом."""
    with pytest.raises(TypeError):
        _ = first_product + 10  # type: ignore
