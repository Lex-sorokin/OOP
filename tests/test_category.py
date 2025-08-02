import pytest

from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert first_category.description == (
        "Смартфоны, как средство не только коммуникации,\n" "но и получение дополнительных функций для удобства жизни"
    )
    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_add_product(first_product: Product) -> None:
    assert first_product.name == "Iphone 15"
    assert first_product.description == "512GB, Gray space"
    assert first_product.price == 210000.0
    assert first_product.quantity == 8


def test_product(first_category: Category, first_product: Product, second_product: Product) -> None:
    first_category.add_product(first_product)
    first_category.add_product(second_product)
    expected_str = "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    assert first_category.products == expected_str


def test_add_wrong_type_product() -> None:
    category = Category("Игрушки", "Категория с игрушками", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")  # type: ignore[arg-type]
