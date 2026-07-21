from src.constants.messages import MSG


class ZeroQuantityError(Exception):
    """Исключение при попытке добавить товар с нулевым количеством."""

    def __init__(self) -> None:
        super().__init__(MSG.ZERO_QUANTITY)
