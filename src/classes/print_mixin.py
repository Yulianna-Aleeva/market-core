class PrintMixin:
    """Миксин печатает информацию о созданном объекте."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает строку вида Class(param1, param2, ...)."""
        params = ", ".join(repr(v) for v in self.__dict__.values())
        return f"{self.__class__.__name__}({params})"
