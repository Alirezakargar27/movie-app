import requests
import random

api_key = '188c2dda'
OMDB_API_URL = f'http://www.omdbapi.com/?apikey={api_key}'

class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return
        print(f"{len(movies)} movies in total")
        for title, info in movies.items():
            print(f"{title}: Rating - {info['rating']}, Year of Release - {info['year']}, Poster URL - {info['poster_url']}")

    def _command_add_movie(self):
        title = input("Please write the name of the movie: ")
        try:
            response = requests.get(f"{OMDB_API_URL}&t={title}")
            response.raise_for_status()
            movie_data = response.json()
            if movie_data.get('Response') == 'True':
                year = movie_data.get('Year')
                rating = movie_data.get('imdbRating')
                if rating != 'N/A':
                    rating = float(rating)
                else:
                    rating = None
                poster_url = movie_data.get('Poster')
                self._storage.add_movie(title, year, rating, poster_url)
                print(f"Movie '{title}' successfully added")
            else:
                print(f"Movie '{title}' not found in the database.")
        except requests.RequestException as e:
            print("Error accessing the OMDb API:", e)
            print("Please check your internet connection and try again.")

    def _command_delete_movie(self):
        title = input("Please write the name of the movie you want to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        title = input("Please write the name of the movie you want to update: ")
        rating = float(input("Please enter the new rating for the movie: "))
        self._storage.update_movie(title, rating)

    def _command_statistics(self):
        movies = self._storage.list_movies()
        total_movies = len(movies)
        if total_movies == 0:
            print("No movies in the database.")
            return
        total_ratings = sum(info['rating'] for info in movies.values() if info['rating'] is not None)
        average_rating = total_ratings / total_movies
        print(f"Total number of movies: {total_movies}")
        print(f"Average rating of movies: {average_rating:.2f}")

    def _command_random_movie(self):
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return
        random_title = random.choice(list(movies.keys()))
        print(f"Random movie: {random_title}")

    def _command_search_movie(self):
        title = input("Please enter the title of the movie: ")
        movies = self._storage.list_movies()
        if title in movies:
            info = movies[title]
            print(f"{title}: Rating - {info['rating']}, Year of Release - {info['year']}, Poster URL - {info['poster_url']}")
        else:
            print(f"Movie '{title}' not found in the database.")

    def _command_movies_sorted_by_rating(self):
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'] if x[1]['rating'] is not None else 0, reverse=True)
        for title, info in sorted_movies:
            print(f"{title}: Rating - {info['rating']}, Year of Release - {info['year']}, Poster URL - {info['poster_url']}")

    def _generate_website(self):
        with open("index_template.html", "r") as template_file:
            template = template_file.read()
        movie_grid_html = ""
        movies = self._storage.list_movies()
        for title, info in movies.items():
            movie_grid_html += f"<li class='movie'><img src='{info['poster_url']}' alt='{title}' class='movie-poster'><div class='movie-title'>{title}</div><div class='movie-year'>{info['year']}</div></li>"
        template = template.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)
        with open("index.html", "w") as output_file:
            output_file.write(template)
        print("Website was generated successfully.")

    def run(self):
        while True:
            self._display_menu()
            choice = input("Enter your choice: ")
            if choice == '0':
                print("Bye!")
                break
            elif choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_delete_movie()
            elif choice == '4':
                self._command_update_movie()
            elif choice == '5':
                self._command_statistics()
            elif choice == '6':
                self._command_random_movie()
            elif choice == '7':
                self._command_search_movie()
            elif choice == '8':
                self._command_movies_sorted_by_rating()
            elif choice == '9':
                self._generate_website()
            else:
                print("Invalid choice. Please try again.")

    def _display_menu(self):
        print("\nMenu:")
        print("0. Exit")
        print("1. List Movies")
        print("2. Add Movie")
        print("3. Delete Movie")
        print("4. Update Movie")
        print("5. Statistics")
        print("6. Random Movie")
        print("7. Search Movie")
        print("8. Movies Sorted by Rating (Descending)")
        print("9. Generate Website")
