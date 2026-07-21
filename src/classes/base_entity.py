from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Абстрактный базовый класс с товарами (категория, заказ)."""

    @abstractmethod
    def __init__(self, name: str, description: str) -> None:
        """Задаёт название и описание."""
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает текст для пользователя."""
        ...
