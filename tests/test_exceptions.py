from src.classes.exceptions import ZeroQuantityError
from src.constants.messages import MSG


def test_zero_quantity_error_default_message() -> None:
    """Проверка сообщения по умолчанию у ZeroQuantityError."""
    error = ZeroQuantityError()
    assert str(error) == MSG.ZERO_QUANTITY
