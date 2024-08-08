from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999,
            "poster_url": "..."
          },
          "..." {
            ...
          },
        }
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster_url):
        """
        Adds a movie to the movies database.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        """
        pass
