class Movie:
    """
    A movie available for rent.
    """
    
    def __init__(self, title, price_strategy):
        # Initialize a new movie. 
        self.title = title
        self.price_strategy = price_strategy

    def get_price(self, days_rented):
        """Compute the rental price based on the movie type."""
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented):
        """Compute the frequent renter points for the rental."""
        return self.price_strategy.get_rental_points(days_rented)
    
    def get_title(self):
        """Return title of a movie."""
        return self.title
    
    def __str__(self):
        return self.title
