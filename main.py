from movie import *
from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog


def make_movies():
    """Some sample movies with associated price strategies."""
    movies = [
        Movie("Air",
              2023,
              ["drama", "biography", "sports"],
              NEW_RELEASE_PRICE),

        Movie("Oppenheimer",
              2023,
              ["drama", "history", "biography"],
              REGULAR_PRICE),

        Movie("Frozen",
              2013,
              ["animation", "family", "fantasy"],
              CHILDREN_PRICE),

        Movie("Bitconned",
              2023,
              ["comedy", "thriller"],
              NEW_RELEASE_PRICE),

        Movie("Particle Fever",
              2013,
              ["documentary", "science"],
              REGULAR_PRICE)
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
