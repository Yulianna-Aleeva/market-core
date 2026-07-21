import json
from pathlib import Path

from src.classes.category import Category
from src.classes.product import Product


def read_categories_from_json(filepath: str | Path) -> list[Category]:
    """Чтение данных из JSON и создание объектов Category и Product."""
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    category_objects = []
    for cat_data in data:
        products = [Product.new_product(prod_data) for prod_data in cat_data.get("products", [])]
        category_objects.append(Category(cat_data["name"], cat_data["description"], products))

    return category_objects


if __name__ == "__main__":  # pragma: no cover
    Category.category_count = 0
    Category.product_count = 0

    base_dir = Path(__file__).resolve().parents[2]
    json_path = base_dir / "data" / "products.json"

    for cat in read_categories_from_json(json_path):
        print(f"\nКатегория: {cat.name}")
        print(f"Описание: {cat.description}")
        print(f"Количество товаров: {len(cat.products)}")
        print(cat.products)

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
