from src.classes.smartphone import Smartphone


def test_smartphone_init(smartphone: Smartphone, category_data: list[dict]) -> None:
    """Корректная инициализация объекта Smartphone."""
    d = category_data[0]["products"][0]

    assert smartphone.name == d["name"]
    assert smartphone.description == d["description"]
    assert smartphone.price == d["price"]
    assert smartphone.quantity == d["quantity"]
    assert smartphone.efficiency == d["efficiency"]
    assert smartphone.model == d["model"]
    assert smartphone.memory == d["memory"]
    assert smartphone.color == d["color"]
