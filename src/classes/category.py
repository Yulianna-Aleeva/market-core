from src.classes.base_entity import BaseEntity
from src.classes.exceptions import ZeroQuantityError
from src.classes.product import Product
from src.constants.messages import MSG


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
        if not isinstance(product, Product):
            raise TypeError(MSG.INVALID_TYPE)

        try:  # если количество = 0, сразу выбрасывается ошибка и товар не создаётся
            if product.quantity == 0:
                raise ZeroQuantityError
            self.__products.append(product)
            Category.product_count += 1
        except ZeroQuantityError as e:
            print(e)
        else:
            print(MSG.PRODUCT_ADDED)
        finally:
            print(MSG.PROCESSING_FINISHED)

    def middle_price(self) -> float:
        """Возвращает средний ценник всех товаров категории."""
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:  # геттер списка товаров
        return "".join(f"{str(p)}\n" for p in self.__products)
