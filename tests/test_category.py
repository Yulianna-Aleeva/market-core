def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 1
    assert first_category.products[0].name == "Samsung Galaxy C23 Ultra"
    assert first_category.products[0].description == "256GB, Серый цвет, 200MP камера"
    assert first_category.products[0].price == 180000.0
    assert first_category.products[0].quantity == 5
    assert first_category.category_count == 2
    assert first_category.product_count == 12
    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(second_category.products) == 1
    assert second_category.products[0].name == '55" QLED 4K'
    assert second_category.products[0].description == "Фоновая подсветка"
    assert second_category.products[0].price == 123000.0
    assert second_category.products[0].quantity == 7
    assert second_category.category_count == 2
    assert second_category.product_count == 12
