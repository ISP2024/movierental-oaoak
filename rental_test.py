import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing_strategy import RegularPriceStrategy, ChildrensPriceStrategy, NewReleasePriceStrategy


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.regular_movie = Movie("Air", RegularPriceStrategy())
        self.childrens_movie = Movie("Frozen", ChildrensPriceStrategy())
        self.new_release_movie = Movie("Dune", NewReleasePriceStrategy())

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", RegularPriceStrategy())
        self.assertEqual("Air", m.get_title())
        self.assertIsInstance(m.price_strategy, RegularPriceStrategy)

    def test_rental_price_new_release(self):
        """Test price calculation for New Release movies"""
        rental = Rental(self.new_release_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_release_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

    def test_rental_price_regular(self):
        """Test price calculation for Regular movies"""
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)

    def test_rental_price_childrens(self):
        """Test price calculation for Children's movies"""
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points_new_release(self):
        """Test frequent renter points for New Release movies"""
        rental = Rental(self.new_release_movie, 3)
        self.assertEqual(rental.get_rental_points(), 3)

    def test_rental_points_regular(self):
        """Test frequent renter points for Regular movies"""
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)

    def test_rental_points_childrens(self):
        """Test frequent renter points for Children's movies"""
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)


if __name__ == '__main__':
    unittest.main()
