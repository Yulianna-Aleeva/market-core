from src.classes.product import Product


class Category:
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        self.name = name  # название категории
        self.description = description  # описание категории
        self.products = products if products else []  # список товаров категории
        Category.category_count += 1
        Category.product_count += len(self.products)
