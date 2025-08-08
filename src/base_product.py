from abc import ABC, abstractmethod
from typing import Self


class BaseProduct(ABC):
    """
    Базовый абстрактный класс
    """
    @classmethod
    @abstractmethod
    def new_product(cls, new_product: dict) -> Self:
        pass
