from pathlib import Path

from src.classes.category import Category
from src.classes.product import Product
from src.utils.read_json import read_categories_from_json


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


# === ПРОВЕРКА КОДА ===
if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parents[2]
    json_path = base_dir / "data" / "products.json"

    categories = read_categories_from_json(json_path)
    first_category = categories[0]

    print(f"Товары из категории '{first_category.name}':")
    iterator = CategoryIterator(first_category)
    for i, p in enumerate(iterator, start=1):
        print(f"{i}. {p.name} | {p.price} руб. | {p.quantity} шт.")
