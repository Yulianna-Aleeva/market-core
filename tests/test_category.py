from src.category import Category


def test_category_init(first_category: Category, second_category: Category, category_data: list[dict]) -> None:
    """Корректная инициализация объектов Category."""
    first_data = category_data[0]
    second_data = category_data[1]

    assert first_category.name == first_data["name"]
    assert second_category.description == second_data["description"]
    assert len(first_category.products) == len(first_data["products"])
    assert len(second_category.products) == len(second_data["products"])


def test_category_init_empty_products() -> None:
    """Инициализация категории без передачи списка товаров."""
    category = Category("Пустая", "Без товаров")
    assert category.products == []


def test_category_counts(first_category: Category, second_category: Category, category_data: list[dict]) -> None:
    """Динамическая проверка подсчета количества категорий и товаров."""
    # Вычисляем ожидаемые значения из фикстуры category_data
    expected_category_count = len(category_data)
    expected_product_count = sum(len(category["products"]) for category in category_data)

    assert Category.category_count == expected_category_count
    assert Category.product_count == expected_product_count
