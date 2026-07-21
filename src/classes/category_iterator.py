from src.classes.category import Category
from src.classes.product import Product


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        products: list[Product] = self.category._Category__products  # type: ignore # noqa
        if self.index < len(products):
            product = products[self.index]
            self.index += 1
            return product
        raise StopIteration
