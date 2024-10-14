import unittest
from rental import Rental
from movie import Movie, REGULAR_PRICE, NEW_RELEASE_PRICE, CHILDREN_PRICE

class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", NEW_RELEASE_PRICE)
        self.regular_movie = Movie("Air", REGULAR_PRICE)
        self.childrens_movie = Movie("Frozen", CHILDREN_PRICE)

    def test_movie_attributes(self):
        """Test movie attributes for correctness after refactoring."""
        m = Movie("Air", REGULAR_PRICE)
        self.assertEqual("Air", m.get_title())
        self.assertIs(m.price_strategy, REGULAR_PRICE)

    def test_rental_price(self):
        """Test rental price calculations for different movies."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)

        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.new_movie, 2)
        self.assertEqual(rental.get_price(), 6.0)

        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)

    def test_rental_points(self):
        """Test rental points calculation for different movies."""
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)

        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_rental_points(), 1)


if __name__ == '__main__':
    unittest.main()
