from src.product import Product


class Category:
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in self.products)
