import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from pricing_strategy import NewReleasePriceStrategy, ChildrensPriceStrategy, RegularPriceStrategy

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", NewReleasePriceStrategy())
        self.regular_movie = Movie("CitizenFour", RegularPriceStrategy())
        self.childrens_movie = Movie("Frozen", ChildrensPriceStrategy())

    @unittest.skip("No convenient way to test")
    def test_billing():
        # no convenient way to test billing since its buried in the statement() method.
        pass
    
    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_charge(self):
        """Test total charge for a collection of rentals."""
        rental1 = Rental(self.new_movie, 3)
        rental2 = Rental(self.regular_movie, 4)
        rental3 = Rental(self.childrens_movie, 5)

        self.c.add_rental(rental1)
        self.c.add_rental(rental2)
        self.c.add_rental(rental3)

        self.assertEqual(self.c.total_charge(), 18.5)
