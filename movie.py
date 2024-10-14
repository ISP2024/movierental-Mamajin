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


# Create instances of the strategies (singleton-like, since they have no state)
REGULAR_PRICE = RegularPrice()
NEW_RELEASE_PRICE = NewReleasePrice()
CHILDREN_PRICE = ChildrenPrice()


class Movie:
    """A movie available for rent."""

    def __init__(self, title, price_strategy: PriceStrategy):
        """Initialize a new movie with a price strategy."""
        self.title = title
        self.price_strategy = price_strategy

    def get_price(self, days_rented: int) -> float:
        """Delegate the price calculation to the price strategy."""
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented: int) -> int:
        """Delegate the frequent renter points calculation to the price strategy."""
        return self.price_strategy.get_rental_points(days_rented)

    def get_title(self) -> str:
        return self.title

