from src.classes.product import Product


class Category:
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: list[Product] | None = None) -> None:
        self.name = name  # название категории
        self.description = description  # описание категории
        self.__products = products if products else []  # приватный список товаров категории
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:  # добавление товара
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:  # геттер списка товаров
        return "".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products)
