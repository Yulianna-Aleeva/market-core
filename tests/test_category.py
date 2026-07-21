import pytest

from src.classes.category import Category
from src.classes.product import Product
from src.constants.messages import MSG


def test_category_init(first_category: Category, second_category: Category, category_data: list[dict]) -> None:
    """Корректная инициализация объектов Category."""
    first_data = category_data[0]
    second_data = category_data[1]

    assert first_category.name == first_data["name"]
    assert second_category.description == second_data["description"]


def test_category_products_property(first_category: Category, category_data: list[dict]) -> None:
    """Геттер products возвращает строку нужного формата, собранную из фикстуры."""
    products_data = category_data[0]["products"]
    expected = "".join(f'{p["name"]}, {p["price"]} руб. Остаток: {p["quantity"]} шт.\n' for p in products_data)
    assert first_category.products == expected


def test_category_init_empty_products() -> None:
    """Инициализация категории без передачи списка товаров."""
    category = Category("Пустая", "Без товаров")
    assert category.products == ""


def test_category_counts(first_category: Category, second_category: Category, category_data: list[dict]) -> None:
    """Динамическая проверка подсчета количества категорий и товаров."""
    # Вычисляем ожидаемые значения из фикстуры category_data
    expected_category_count = len(category_data)
    expected_product_count = sum(len(category["products"]) for category in category_data)

    assert Category.category_count == expected_category_count
    assert Category.product_count == expected_product_count


def test_category_add_product(first_category: Category, second_product: Product) -> None:
    """Динамическая проверка добавления товара в категорию."""
    initial_product_count = Category.product_count

    first_category.add_product(second_product)

    # Проверяем, что товар появился в строке вывода
    assert second_product.name in first_category.products
    # Проверяем, что общий счетчик товаров увеличился ровно на 1
    assert Category.product_count == initial_product_count + 1


def test_category_second_products_property(second_category: Category, category_data: list[dict]) -> None:
    """Геттер products возвращает строку нужного формата."""
    expected = (
        f"{category_data[1]['products'][0]['name']}, "
        f"{category_data[1]['products'][0]['price']} руб. "
        f"Остаток: {category_data[1]['products'][0]['quantity']} шт.\n"
    )
    assert second_category.products == expected


def test_category_str(first_category: Category, category_data: list[dict]) -> None:
    """Возвращает строку с названием категории и общим количеством товаров."""
    cat_name = category_data[0]["name"]
    total_quantity = sum(p["quantity"] for p in category_data[0]["products"])

    assert str(first_category) == f"{cat_name}, количество продуктов: {total_quantity} шт."


def test_category_str_empty() -> None:
    """Возвращает строку для категории без товаров (должно быть 0 шт.)."""
    category = Category("Пустая", "Без товаров")
    assert str(category) == "Пустая, количество продуктов: 0 шт."


def test_category_middle_price(
    first_product: Product,
    second_product: Product,
    category_data: list[dict],
) -> None:
    """Средний ценник равен средне-арифметическому цен всех товаров."""
    products = [first_product, second_product]
    source = category_data[0]
    category = Category(source["name"], source["description"], products)

    expected = round(sum(p.price for p in products) / len(products), 2)
    assert category.middle_price() == expected


def test_category_middle_price_single_product(first_product: Product, category_data: list[dict]) -> None:
    """Средний ценник категории с одним товаром равен его цене."""
    source = category_data[0]
    category = Category(source["name"], source["description"], [first_product])

    assert category.middle_price() == first_product.price


def test_category_middle_price_empty() -> None:
    """Средний ценник пустой категории равен нулю."""
    empty_products: list[Product] = []
    category = Category("Пустая", "Без товаров", empty_products)

    assert category.middle_price() == len(empty_products)


def test_add_product_success_messages(
    first_category: Category,
    second_product: Product,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """При успешном добавлении выводятся сообщения из MSG."""
    first_category.add_product(second_product)
    captured = capsys.readouterr()

    assert second_product.name in first_category.products
    assert MSG.PRODUCT_ADDED in captured.out
    assert MSG.PROCESSING_FINISHED in captured.out


def test_add_product_zero_quantity(
    first_category: Category,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """При добавлении товара с нулевым количеством выводятся сообщения из MSG."""

    class FakeProduct:
        quantity = len([])

    first_category.add_product(FakeProduct())  # type: ignore
    captured = capsys.readouterr()

    assert MSG.ZERO_QUANTITY in captured.out
    assert MSG.PROCESSING_FINISHED in captured.out
    assert MSG.PRODUCT_ADDED not in captured.out
