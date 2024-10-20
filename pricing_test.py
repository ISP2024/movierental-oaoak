import unittest
from movie import Movie
from rental import Rental
from pricing import *


class TestPriceStrategy(unittest.TestCase):

    def test_new_release(self):
        movie = Movie("Top Gun: Maverick", 2024, ["Action"], price_strategy=NewReleasePriceStrategy())
        rental = Rental(movie, days_rented=3)
        self.assertEqual(rental.get_price(), NewReleasePriceStrategy().get_price(3))

    def test_childrens_movie(self):
        movie = Movie("Finding Nemo", 2003, ["Children", "Animation"], price_strategy=ChildrensPriceStrategy())
        rental = Rental(movie, days_rented=5)
        self.assertEqual(rental.get_price(), ChildrensPriceStrategy().get_price(5))

    def test_regular_movie(self):
        movie = Movie("The Godfather", 1972, ["Drama"], price_strategy=RegularPriceStrategy())
        rental = Rental(movie, days_rented=2)
        self.assertEqual(rental.get_price(), RegularPriceStrategy().get_price(2))

    def test_childrens_alternate_spelling(self):
        movie = Movie("Some Movie", 1990, ["Childrens"], price_strategy=ChildrensPriceStrategy())
        rental = Rental(movie, days_rented=3)
        self.assertEqual(rental.get_price(), ChildrensPriceStrategy().get_price(3))


if __name__ == "__main__":
    unittest.main()
