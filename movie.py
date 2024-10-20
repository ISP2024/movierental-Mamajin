from price_strategy import PriceStrategy, RegularPrice, NewReleasePrice, \
    ChildrenPrice

# Create instances of the strategies (singleton-like, since they have no state)
REGULAR_PRICE = RegularPrice()
NEW_RELEASE_PRICE = NewReleasePrice()
CHILDREN_PRICE = ChildrenPrice()


class Movie:
    """A movie available for rent, with immutable attributes."""

    def __init__(self, title: str, year: int, genres: list[str], price_strategy: PriceStrategy):
        """Initialize a new movie with a price strategy, year, and genre."""
        self._title = title
        self._year = year
        # Using frozenset to make it immutable
        self._genres = frozenset(genres)
        self._price_strategy = price_strategy

    @property
    def title(self) -> str:
        """Return the title of the movie."""
        return self._title

    @property
    def year(self) -> int:
        """Return the year the movie was released."""
        return self._year

    @property
    def genres(self) -> frozenset:
        """Return the genres of the movie."""
        return self._genres

    @property
    def price_strategy(self) -> PriceStrategy:
        """Return the price strategy of the movie."""
        return self._price_strategy

    def get_title(self):
        return self.title

    def is_genre(self, genre: str) -> bool:
        """Check if the movie belongs to the specified genre (case-insensitive)."""
        return genre.lower() in map(str.lower, self._genres)

    def __str__(self) -> str:
        """Return the string representation of the movie."""
        return f"{self._title} ({self._year})"
