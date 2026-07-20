import pytest

from src.classes.base_product import BaseProduct


def test_base_product_is_abstract() -> None:
    """Нельзя создать экземпляр абстрактного класса BaseProduct."""
    with pytest.raises(TypeError):
        BaseProduct("Товар", "Описание", 100.0, 5)  # type: ignore


def test_base_product_subclass_must_implement_methods() -> None:
    """Подкласс без реализации абстрактных методов нельзя создать."""

    class Incomplete(BaseProduct):
        pass

    with pytest.raises(TypeError):
        Incomplete()  # type: ignore
