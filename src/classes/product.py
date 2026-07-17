class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # название товара
        self.description = description  # описание товара
        self.price = price  # цена товара
        self.quantity = quantity  # количество товаров в наличии
