import logging
import csv
from movie import *
from typing import Optional, List, Set


# Configure logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


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

            for line_number, row in enumerate(reader, start=1):
                # Skip blank lines and comment lines
                if not row or row[0].startswith('#'):
                    continue

                if len(row) < 4:  # Ensure there are enough columns
                    logging.error(f"Line {line_number}: Unrecognized format {row}")
                    continue  # Skip this iteration if row is invalid

                try:
                    # Assuming columns are in the order: movie_id, title, year, genres
                    movie_id = row[0]
                    title = row[1]  # title is in the second column
                    year = int(row[2])
                    genres = row[3].split('|')

                    price_strategy = self.determine_price_strategy(year, genres)

                    # Create and store the movie object
                    movie = Movie(title, year, genres, price_strategy)
                    self.movies.append(movie)

                except (ValueError, IndexError) as e:
                    continue

    @staticmethod
    def determine_price_strategy(year: int, genres: list) -> PriceStrategy:
        """Determine the price strategy based on the year and genres."""
        current_year = 2024
        if year == current_year:
            return NEW_RELEASE_PRICE
        elif any("children" in genre.lower() for genre in genres):
            return CHILDREN_PRICE
        else:
            return REGULAR_PRICE

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional['Movie']:
        """Return a movie by title and optionally by year."""
        for movie in self.movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None  # Movie not found
