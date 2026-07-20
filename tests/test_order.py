import pytest

from src.classes.base_entity import BaseEntity
from src.classes.order import Order
from src.classes.product import Product


def test_order_init(order: Order, first_product: Product, order_data: dict) -> None:
    """Корректная инициализация Order."""
    assert order.name == order_data["name"]
    assert order.description == order_data["description"]
    assert order.product is first_product
    assert order.quantity == order_data["quantity"]


def test_order_total_price(order: Order, first_product: Product) -> None:
    """Итоговая стоимость считается корректно."""
    assert order.total_price == first_product.price * order.quantity


def test_order_str(order: Order, first_product: Product) -> None:
    """Возвращает текст для пользователя."""
    expected = f"{first_product.name}, количество: {order.quantity} шт., сумма: {order.total_price} руб."
    assert str(order) == expected


def test_order_zero_quantity(first_product: Product, order_data: dict) -> None:
    """Заказ с нулевым количеством: итоговая стоимость 0."""
    order = Order(order_data["name"], order_data["description"], first_product, 0)
    assert order.total_price == 0
    assert order.quantity == 0


def test_base_entity_is_abstract() -> None:
    """Нельзя создать экземпляр абстрактного класса BaseEntity."""
    with pytest.raises(TypeError):
        BaseEntity("Название", "Описание")  # type: ignore
