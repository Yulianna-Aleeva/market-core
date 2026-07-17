import json
import tempfile

import pytest

from src.category import Category
from src.product import Product
from src.utils import read_json


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name='55" QLED 4K',
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7,
    )


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
        ),
        products=[
            Product(
                name="Samsung Galaxy C23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            )
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        ),
        products=[
            Product(
                name='55" QLED 4K',
                description="Фоновая подсветка",
                price=123000.0,
                quantity=7,
            )
        ],
    )


@pytest.fixture
def mock_json_data():
    return [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации,"
                "но и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        },
        {
            "name": "Телевизоры",
            "description": (
                "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
            ),
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]


@pytest.fixture
def json_file(mock_json_data):
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        json.dump(mock_json_data, f)
        return f.name


@pytest.fixture
def loaded_data(json_file):
    return read_json(json_file)
