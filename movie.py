from price_strategy import PriceStrategy, RegularPrice, NewReleasePrice, \
    ChildrenPrice

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

    def get_title(self) -> str:
        return self.title

