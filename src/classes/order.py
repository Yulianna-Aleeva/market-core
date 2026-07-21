from src.classes.base_entity import BaseEntity
from src.classes.product import Product


class Order(BaseEntity):
    """Заказ с одним товаром."""

    def __init__(self, name: str, description: str, product: Product, quantity: int) -> None:
        self.name = name  # название заказа
        self.description = description  # описание заказа
        self.product = product  # купленный товар
        self.quantity = quantity  # количество
        self.total_price = product.price * quantity  # итоговая стоимость

    def __str__(self) -> str:
        """Возвращает текст для пользователя."""
        return f"{self.product.name}, количество: {self.quantity} шт., сумма: {self.total_price} руб."
