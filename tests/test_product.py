import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.product import LawnGrass, Product, Smartphone


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8
    assert str(first_product) == "Iphone 15, 210000.0 Остаток: 8 шт."


def test_getter_setter_price(monkeypatch: MonkeyPatch) -> None:
    p = Product("Item", "Test item", 1000.0, 1)

    # Повышаем цену
    p.price = 1500.0
    assert p.price == 1500.0

    # Нулевая цена не проходит
    p.price = 0
    assert p.price == 1500.0

    # Отрицательная цена не проходит
    p.price = -10
    assert p.price == 1500.0

    # Подтверждение понижения цены отказ
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 900.0
    assert p.price == 1500.0

    # Подтверждение понижения цены согласие
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 900.0
    assert p.price == 900.0


def test_new_product() -> None:
    n_product = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый", "price": 180000.0, "quantity": 5}
    product = Product.new_product(n_product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert isinstance(product, Product)


def test_print_product() -> None:
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    assert str(grass1) == "Газонная трава, Элитная трава для газона, Россия, 7 дней, Зеленый, 500.0, Остаток: 20 шт."
    assert str(smartphone2) == "Iphone 15, 512GB, Gray space, 98.2, 15, 512, Gray space, 210000.0, Остаток: 8 шт."


def test_add_new_category_product(grass_category: LawnGrass, smartphone_category: Smartphone) -> None:
    """
    Тест на сложение новых продуктов в новых категориях
    """
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    assert grass1 + grass2 == 16750.0
    assert smartphone1 + smartphone2 == 2580000.0

    with pytest.raises(TypeError):
        smartphone1 + grass1
