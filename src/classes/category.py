from src.classes.base_entity import BaseEntity
from src.classes.product import Product


class Category(BaseEntity):
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        self.name = name  # название категории
        self.description = description  # описание категории
        self.__products = products if products else []  # приватный список товаров категории
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Возвращает название категории и общее количество товаров."""
        return f"{self.name}, количество продуктов: {sum(p.quantity for p in self.__products)} шт."

    def add_product(self, product: Product) -> None:  # добавление товара
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        """Возвращает средний ценник всех товаров категории."""
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:  # геттер списка товаров
        return "".join(f"{str(p)}\n" for p in self.__products)
