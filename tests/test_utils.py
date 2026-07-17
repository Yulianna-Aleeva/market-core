import json
from unittest.mock import mock_open, patch

from src.utils.utils import read_categories_from_json


def test_read_categories_from_json(category_data: list[dict]) -> None:
    """Проверка загрузки категорий из JSON с использованием фикстуры."""
    # Превращаем фикстуру обратно в строку JSON (для имитации файла)
    mock_json_data = json.dumps(category_data)

    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_categories_from_json("fake_path.json")

    assert len(result) == len(category_data)
    assert result[0].name == category_data[0]["name"]
    assert len(result[0].products) == len(category_data[0]["products"])
    assert result[1].products[0].name == category_data[1]["products"][0]["name"]


def test_read_empty_json() -> None:
    """Пустой JSON-файл (список категорий)."""
    with patch("builtins.open", mock_open(read_data="[]")):
        result = read_categories_from_json("fake_path.json")
    assert result == []


def test_read_category_without_products() -> None:
    """Категория без ключа products."""
    mock_data = '[{"name": "Пустая", "description": "Без товаров"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_categories_from_json("fake_path.json")
    assert len(result) == 1
    assert result[0].products == []
