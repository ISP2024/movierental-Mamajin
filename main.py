from movie import *
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies with associated price strategies."""
    movies = [
        Movie("Air", NEW_RELEASE_PRICE),
        Movie("Oppenheimer", REGULAR_PRICE),
        Movie("Frozen", CHILDREN_PRICE),
        Movie("Bitconned", NEW_RELEASE_PRICE),
        Movie("Particle Fever", REGULAR_PRICE)
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
