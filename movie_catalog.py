from movie import *
import csv
from typing import Optional, List, Set


class MovieCatalog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'movies'):
            self.movies = []  # Store Movie objects
            self.load_movies()

    def load_movies(self):
        """Load movies from a CSV file into memory as Movie objects."""
        with open('movies.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                title = row[0]
                year = int(row[1])
                genres = row[2].split(';')  # Assume genres are separated by ';'
                price_strategy = self.get_price_strategy(row[3])  # Assume a column for price code
                movie = Movie(title, year, genres, price_strategy)
                self.movies.append(movie)

    def get_price_strategy(self, price_code: str):
        """Return the corresponding PriceStrategy based on the price code."""
        if price_code == "regular":
            return REGULAR_PRICE
        elif price_code == "new_release":
            return NEW_RELEASE_PRICE
        elif price_code == "children":
            return CHILDREN_PRICE
        else:
            raise ValueError(f"Unknown price code: {price_code}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional['Movie']:
        """Return a movie by title and optionally by year."""
        for movie in self.movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None  # Movie not found