import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:
    	
    	c = a customer
    	movies = list of some movies
    	"""
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_billing(self):
        # no convenient way to test billing since its buried in the statement() method.
        self.c.add_rental(Rental(self.new_movie, 2))
        self.c.add_rental(Rental(self.regular_movie, 5))
        self.c.add_rental(Rental(self.childrens_movie, 7))
        total_bill = self.c.total_amount()[0]
        self.assertEqual(20.0, total_bill)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
