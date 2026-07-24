import pytest

from src.classes.category import Category
from src.classes.lawn_grass import LawnGrass
from src.classes.order import Order
from src.classes.product import Product
from src.classes.smartphone import Smartphone


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
                    "efficiency": 95.5,
                    "model": "S23 Ultra",
                    "memory": 256,
                    "color": "Серый",
                }
            ],
        },
        {
            "name": "Газонная трава",
            "description": "Различные виды газонной травы",
            "products": [
                {
                    "name": "Газонная трава",
                    "description": "Элитная трава для газона",
                    "price": 500.0,
                    "quantity": 20,
                    "country": "Россия",
                    "germination_period": "7 дней",
                    "color": "Зеленый",
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
def smartphone(category_data: list[dict]) -> Smartphone:
    """Экземпляр Smartphone из данных."""
    d = category_data[0]["products"][0]
    return Smartphone(
        d["name"],
        d["description"],
        d["price"],
        d["quantity"],
        d["efficiency"],
        d["model"],
        d["memory"],
        d["color"],
    )


@pytest.fixture
def lawn_grass(category_data: list[dict]) -> LawnGrass:
    """Экземпляр LawnGrass из данных."""
    d = category_data[1]["products"][0]
    return LawnGrass(
        d["name"],
        d["description"],
        d["price"],
        d["quantity"],
        d["country"],
        d["germination_period"],
        d["color"],
    )


@pytest.fixture
def order_data() -> dict:
    """Данные для заказа."""
    return {"name": "Заказ №1", "description": "Тестовый заказ", "quantity": 2}


@pytest.fixture
def order(first_product: Product, order_data: dict) -> Order:
    """Заказ на первый продукт."""
    return Order(order_data["name"], order_data["description"], first_product, order_data["quantity"])
