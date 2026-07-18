from src.classes.category import Category
from src.classes.product import Product


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
