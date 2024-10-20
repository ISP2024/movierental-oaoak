from dataclasses import dataclass, field
from typing import Collection
from pricing import *


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str] = field(default_factory=list)
    price_strategy: PriceStrategy = field(default_factory=PriceStrategy)
    
    def is_genre(self, genre: str) -> bool:
        """Check if the movie belongs to a given genre."""
        return genre.lower() in (g.lower() for g in self.genre)

    def __str__(self):
        """Return the string representation of the movie as 'Title (year)'."""
        return f"{self.title} ({self.year})"


if __name__ == '__main__':
    movie = Movie("Mulan", 2020, ["Action", "Adventure", "Drama"])
    print(movie)