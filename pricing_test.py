import unittest
from movie import *


class TestMoviePriceCode(unittest.TestCase):

    def test_new_release(self):
        movie = Movie("New Movie", 2024, ["Action"])
        self.assertIs(movie.price_code_for_movie(movie), NEW_RELEASE_PRICE)

    def test_children_movie(self):
        movie = Movie("Kids Movie", 2020, ["Children"])
        self.assertIs(movie.price_code_for_movie(movie), CHILDREN_PRICE)

    def test_regular_movie(self):
        movie = Movie("Old Movie", 2020, ["Drama"])
        self.assertIs(movie.price_code_for_movie(movie), REGULAR_PRICE)

    def test_case_insensitive_genre(self):
        movie = Movie("Mixed Genre Movie", 2019, ["childrens", "Action"])
        self.assertIs(movie.price_code_for_movie(movie), CHILDREN_PRICE)

if __name__ == '__main__':
    unittest.main()
