from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @abstractmethod
    def __init__(self, *args: object, **kwargs: object) -> None:
        """Создаёт товар с данными: название, описание, цена, количество."""
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает текст для пользователя."""
        ...

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict) -> "BaseProduct":
        """Создает товар из словаря."""
        ...
