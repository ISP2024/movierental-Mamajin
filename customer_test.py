import re
import unittest
from customer import Customer
from rental import Rental
from movie import *

class CustomerTest(unittest.TestCase):
    """Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:
        - c: a customer
        - Movies: list of movies with different price strategies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", NEW_RELEASE_PRICE)
        self.regular_movie = Movie("CitizenFour", REGULAR_PRICE)
        self.childrens_movie = Movie("Frozen", CHILDREN_PRICE)


    def test_billing(self):
        """Test the total billing amount for multiple rentals."""
        # Add rentals for multiple movies
        self.c.add_rental(Rental(self.new_movie, 2))      # New release, 2 days
        self.c.add_rental(Rental(self.regular_movie, 5))  # Regular movie, 5 days
        self.c.add_rental(Rental(self.childrens_movie, 7))  # Children's movie, 7 days
        total_bill = self.c.total_amount()[0]
        # Expected bill: New release (6), Regular (6.5), Children's (7.5)
        self.assertEqual(20.0, total_bill)

    def test_statement(self):
        """Test that the statement format and total charges are correct."""
        # Initial statement, no rentals
        stmt = self.c.statement()
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.search(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])

        # Add a rental and test again
        self.c.add_rental(Rental(self.new_movie, 4))  # New release, 4 days
        stmt = self.c.statement()
        matches = re.search(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])  # 4 days for New release = $12

    def test_regular_movie_points(self):
        """Test frequent renter points for a regular movie rental."""
        rental = Rental(self.regular_movie, 5)  # 5 days rental
        self.assertEqual(rental.get_rental_points(), 1)  # Regular movies always get 1 point

    def test_new_release_movie_points(self):
        """Test frequent renter points for a new release movie rental."""
        rental = Rental(self.new_movie, 3)  # 3 days rental
        self.assertEqual(rental.get_rental_points(), 3)  # 1 point per day for new releases

    def test_children_movie_points(self):
        """Test frequent renter points for a children's movie rental."""
        rental = Rental(self.childrens_movie, 7)  # 7 days rental
        self.assertEqual(rental.get_rental_points(), 1)  # Children's movies always get 1 point
