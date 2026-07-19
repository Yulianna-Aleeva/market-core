from src.classes.lawn_grass import LawnGrass


def test_lawn_grass_init(lawn_grass: LawnGrass, category_data: list[dict]) -> None:
    """Корректная инициализация объекта LawnGrass."""
    d = category_data[1]["products"][0]

    assert lawn_grass.name == d["name"]
    assert lawn_grass.description == d["description"]
    assert lawn_grass.price == d["price"]
    assert lawn_grass.quantity == d["quantity"]
    assert lawn_grass.country == d["country"]
    assert lawn_grass.germination_period == d["germination_period"]
    assert lawn_grass.color == d["color"]
