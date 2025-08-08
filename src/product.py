from typing import Self

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is type(other):
            return float(self.__price * self.quantity + other.__price * other.quantity)
        raise TypeError(f"Нельзя сложить объекты разных классов: {type(self).__name__} и {type(other).__name__}")

    @property
    def price(self) -> float:
        """
        Геттер для получения цены товара.
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер с проверкой, где цена не может быть ≤ 0
        и при снижении цены запрос подтверждения
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = (
                input(f"Вы действительно хотите понизить цену с {self.__price} до {value}? (y/n): ").strip().lower()
            )
            if answer not in "y":
                print("Действие отменено")
                return
            self.__price = value
        else:
            self.__price = value

    @classmethod
    def new_product(cls, new_product: dict) -> Self:
        return cls(
            name=new_product.get("name", ""),
            description=new_product.get("description", ""),
            price=new_product.get("price", 0),
            quantity=new_product.get("quantity", 0),
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.description}, {self.efficiency}, {self.model}, {self.memory}, "
            f"{self.color}, {self.price}, Остаток: {self.quantity} шт."
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.description}, {self.country}, {self.germination_period}, {self.color}, "
            f"{self.price}, Остаток: {self.quantity} шт."
        )
