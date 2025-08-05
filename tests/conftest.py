import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def toys_category() -> Category:
    product1 = Product("Тетрис", "Электронная игрушка", 300.0, 5)
    product2 = Product("Тамагочи", "Электронная игрушка", 200.0, 10)
    product3 = Product("Кубик-рубика", "Аналоговая игрушка", 400.0, 8)
    category = Category("Игрушки", "Категория с игрушками", [product1, product2, product3])
    return category


@pytest.fixture
def grass_category() -> Category:
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])
    return category_grass


@pytest.fixture
def smartphone_category() -> Category:
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    return category_smartphones
