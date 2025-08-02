import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product() -> Product:
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def second_product() -> Product:
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации,\n"
            "но и получение дополнительных функций для удобства жизни"
        ),
        products=[],
    )


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Телевизоры",
        description="""
        Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником
        """,
        products=[],
    )
