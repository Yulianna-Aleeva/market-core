import json
from unittest.mock import mock_open, patch

from src.utils.read_json import read_categories_from_json  # поменяй импорт на свой


def test_read_categories_from_json(category_data: list[dict]) -> None:
    """Проверка загрузки категорий из JSON с использованием фикстуры."""
    # Превращаем фикстуру обратно в строку JSON
    mock_json_data = json.dumps(category_data)

    # Имитируем открытие файла
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_categories_from_json("fake_path.json")

    # Проверяем, что создалось верное количество категорий
    assert len(result) == len(category_data)

    # Сверяем данные каждой категории и её товаров
    for i, category_dict in enumerate(category_data):
        assert result[i].name == category_dict["name"]
        assert result[i].description == category_dict["description"]

        # Проверяем количество строк с товарами через подсчёт переносов строки - "\n"
        expected_product_count = len(category_dict.get("products", []))
        assert result[i].products.count("\n") == expected_product_count

        # Проверяем, что имена товаров попали в итоговую строку геттера
        for product_dict in category_dict.get("products", []):
            assert product_dict["name"] in result[i].products


def test_read_categories_empty_json() -> None:
    """Проверка обработки пустого JSON-файла (пустой список)."""
    with patch("builtins.open", mock_open(read_data="[]")):
        result = read_categories_from_json("fake_path.json")

    assert result == []


def test_read_categories_missing_products_key() -> None:
    """Проверка создания категории, если в JSON отсутствует ключ 'products'."""
    # Создаем минимальный словарь без ключа products
    mock_data = json.dumps([{"name": "Единственная", "description": "Без товаров"}])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_categories_from_json("fake_path.json")

    assert len(result) == 1
    assert result[0].name == "Единственная"
    assert result[0].products == ""  # Геттер должен вернуть пустую строку
