from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days: int) -> float:
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1  # Regular movies always get 1 point


class NewReleasePrice(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days: int) -> float:
        return days * 3  # $3 per day for new releases

    def get_rental_points(self, days: int) -> int:
        return days  # New releases earn 1 point per day


class ChildrenPrice(PriceStrategy):
    """Pricing rules for Children's movies."""

    def get_price(self, days: int) -> float:
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days: int) -> int:
        return 1  # Children's movies always get 1 point
