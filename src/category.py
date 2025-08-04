from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, new_product: Product) -> None:
        """
        Добавляет продукт и увеличивает счетчик
        """
        if not isinstance(new_product, Product):  # ДОБАВЛЕНО: проверка на тип
            raise TypeError("Можно добавить только объект класса Product или его наследника")
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def get_products(self) -> list[Product]:
        return self.__products


class Enumeration:
    """
    Вспомогательный класс для переборки товаров в категории.
    """

    def __init__(self, category: "Category") -> None:
        self.category = category
        self.current_value = -1
        self.stop = len(category.get_products)

    def __iter__(self) -> "Enumeration":
        self.current_value = -1
        return self

    def __next__(self) -> Product:
        if self.current_value + 1 < self.stop:
            self.current_value += 1
            return self.category.get_products[self.current_value]
        else:
            raise StopIteration
