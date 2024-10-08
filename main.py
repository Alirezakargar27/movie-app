from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def main():
    # Uncomment the desired storage type
    storage = StorageJson('movies.json')
    #storage = StorageCsv('movies.csv')

    movie_app = MovieApp(storage)
    movie_app.run()

if __name__ == "__main__":
    main()
