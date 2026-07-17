class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
