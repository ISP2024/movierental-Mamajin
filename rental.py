class Rental:
    """
    A rental of a movie by a customer.
    """

    def __init__(self, movie, days_rented: int):
        """Initialize a new movie rental object."""
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        """Delegate to the movie object to calculate price."""
        return self.movie.get_price(self.days_rented)

    def get_rental_points(self):
        """Delegate to the movie object to calculate rental points."""
        return self.movie.get_rental_points(self.days_rented)
