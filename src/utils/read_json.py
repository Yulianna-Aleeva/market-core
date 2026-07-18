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
