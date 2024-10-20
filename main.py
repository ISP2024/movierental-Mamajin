from movie import *
from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog

# implement later? Currently dead code
catalog = MovieCatalog()


def make_movies():
    """Some sample movies with associated price strategies."""
    movies = [
        catalog.get_movie("Barbie"),
        catalog.get_movie("Young Woman and the Sea"),
        catalog.get_movie("Dumb Money"),
        catalog.get_movie("Son of Saul"),
        catalog.get_movie("Spider Man: No Way Home"),
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
