from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class for price strategies."""

    @abstractmethod
    def get_price(self, days_rented):
        pass

    @abstractmethod
    def get_rental_points(self, days_rented):
        pass


class RegularPriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount

    def get_rental_points(self, days_rented):
        return 1


class ChildrensPriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount

    def get_rental_points(self, days_rented):
        return 1


class NewReleasePriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        return 3 * days_rented

    def get_rental_points(self, days_rented):
        return days_rented