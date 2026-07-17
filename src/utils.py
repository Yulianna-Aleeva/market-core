import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """Читает JSON-файл и возвращает данные в виде списка словарей."""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Преобразует JSON-данные в объекты категорий и продуктов."""
    categories = []
    for cat in data:
        products = []
        for product in cat["products"]:
            products.append(Product(**product))
        cat["products"] = products
        categories.append(Category(**cat))
    return categories


if __name__ == "__main__":  # pragma: no cover
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "data", "products.json")

    raw_data = read_json(json_path)
    categories_data = create_objects_from_json(raw_data)

    for category in categories_data:
        print(category.name)

    print(categories_data[0].product_count)
