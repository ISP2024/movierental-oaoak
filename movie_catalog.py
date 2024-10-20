import csv
import logging
from typing import Optional, List, Dict
from movie import Movie


logging.basicConfig(
    level=logging.ERROR,
    format='Line %(lineno)d: %(message)s'
)

class MovieCatalog:
    """
    Singleton class to manage and create Movie objects from a CSV file.
    """

    _instance = None
    _movies: Dict[str, List[Movie]] = {}

    def __new__(cls):
        """Ensure that only one instance of MovieCatalog is created (singleton pattern)."""
        if cls._instance is None:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._load_movies()
        return cls._instance

    def _load_movies(self):
        """Load movie data from a CSV file. Process one line at a time to avoid loading large files into memory."""
        try:
            with open('movies.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = row['title']
                    try:
                        year = int(row['year'])
                    except Exception:
                        logging.error(f"Unrecognized format {row}")
                        continue
                    genres = row['genres'].split('|')
                    movie = Movie(title, year, genres)
                    if title not in self._movies:
                        self._movies[title] = []
                    self._movies[title].append(movie)
        except FileNotFoundError:
            print("CSV file not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """
        Get the first matching movie by title, and optionally by year.
        If the year is omitted, return the first movie with the matching title.
        """
        if title in self._movies:
            if year:
                for movie in self._movies[title]:
                    if movie.year == year:
                        return movie
            else:
                return self._movies[title][0]
        return None


if __name__ == "__main__":
    catalog = MovieCatalog()
    movie = catalog.get_movie("No Time to Die")
    if movie:
        print(movie)
    else:
        print("Sorry, couldn't find that movie.")
