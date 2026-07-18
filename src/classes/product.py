class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # название товара
        self.description = description  # описание товара
        self.__price = price  # приватная цена товара
        self.quantity = quantity  # количество товаров в наличии

    def __str__(self) -> str:
        """Возвращает строку с данными продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает суммарную стоимость всех товаров двух продуктов."""
        if type(other) is type(self):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @property
    def price(self) -> float:  # геттер цены
        return self.__price

    @price.setter
    def price(self, value: float) -> None:  # сеттер цены
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Создает экземпляр на основе словаря."""
        return cls(data["name"], data["description"], data["price"], data["quantity"])
