from _pytest.monkeypatch import MonkeyPatch

from src.product import Product


def test_product_init(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8


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
