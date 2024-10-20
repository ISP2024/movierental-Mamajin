from movie import *


class Rental:
    """
    A rental of a movie by a customer.
    """

    def __init__(self, movie, days_rented: int):
        """Initialize a new movie rental object."""
        self.movie = movie
        self.days_rented = days_rented
        self.price_strategy = movie.price_strategy

    def get_movie(self):
        """Get movie object"""
        return self.movie

    def get_days_rented(self):
        """Get day rented"""
        return self.days_rented

    def price_code_for_movie(self):
        """Determine the price code based on the movie's attributes."""
        current_year = 2024
        if self.movie.year == current_year:
            return NEW_RELEASE_PRICE
        elif self.movie.is_genre("Children") or self.movie.is_genre("Childrens"):
            return CHILDREN_PRICE
        else:
            return REGULAR_PRICE

    def get_price(self):
        """Delegate to the movie object to calculate price."""
        return self.price_strategy.get_price(self.days_rented)

    def get_rental_points(self):
        """Delegate to the movie object to calculate rental points."""
        return self.price_strategy.get_rental_points(self.days_rented)
