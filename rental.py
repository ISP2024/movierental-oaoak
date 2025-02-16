from pricing import *


class Rental:
    """
    A rental of a movie by a customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application, only days_rented is recorded.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
        a movie with a known rental period (days_rented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.frequent_renter_points = 0
        self.price_code = PriceStrategy.price_code_for_movie(movie)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price_code(self):
        """Return the price code for the rental."""
        return self.price_code

    def get_price(self):
        """Compute rental charge."""
        return self.movie.price_strategy.get_price(self.days_rented)

    def get_rental_points(self):
        """Compute rental points."""
        return self.movie.price_strategy.get_rental_points(self.days_rented)
