import pytest

from src.classes.category import Category
from src.classes.order import Order
from src.classes.product import Product


@pytest.fixture(autouse=True)
def reset_counts() -> None:
    """Автоматический сброс счетчиков перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_data() -> list[dict]:
    """Сырые данные для тестов."""
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
def first_product(category_data: list[dict]) -> Product:
    """Первый продукт из данных."""
    p_data = category_data[0]["products"][0]
    return Product(p_data["name"], p_data["description"], p_data["price"], p_data["quantity"])


@pytest.fixture
def second_product(category_data: list[dict]) -> Product:
    """Второй продукт из данных."""
    p_data = category_data[1]["products"][0]
    return Product(p_data["name"], p_data["description"], p_data["price"], p_data["quantity"])


@pytest.fixture
def first_category(category_data: list[dict], first_product: Product) -> Category:
    """Первая категория из данных."""
    c_data = category_data[0]
    return Category(c_data["name"], c_data["description"], [first_product])


@pytest.fixture
def second_category(category_data: list[dict], second_product: Product) -> Category:
    """Вторая категория из данных."""
    c_data = category_data[1]
    return Category(c_data["name"], c_data["description"], [second_product])


@pytest.fixture
def order_data() -> dict:
    """Данные для заказа."""
    return {"name": "Заказ №1", "description": "Тестовый заказ", "quantity": 2}


@pytest.fixture
def order(first_product: Product, order_data: dict) -> Order:
    """Заказ на первый продукт."""
    return Order(order_data["name"], order_data["description"], first_product, order_data["quantity"])
