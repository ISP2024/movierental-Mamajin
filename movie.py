from pricing import PriceStrategy, RegularPrice, NewReleasePrice, \
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
        self._genres = frozenset(genres)
        self._price_strategy = price_strategy

    @property
    def title(self) -> str:
        return self._title

    @property
    def year(self) -> int:
        return self._year

    @property
    def genres(self) -> frozenset:
        return self._genres

    @property
    def price_strategy(self) -> PriceStrategy:
        return self._price_strategy

    def get_title(self) -> str:
        return self.title

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in map(str.lower, self._genres)

    def __str__(self) -> str:
        return f"{self._title} ({self._year})"

    @classmethod
    def price_code_for_movie(cls, movie: 'Movie') -> PriceStrategy:
        """Determine the price code for the given movie."""
        current_year = 2024  # Replace with dynamic year retrieval if necessary
        if movie.year == current_year:
            return NEW_RELEASE_PRICE
        elif movie.is_genre("Children") or movie.is_genre("Childrens"):
            return CHILDREN_PRICE
        else:
            return REGULAR_PRICE

