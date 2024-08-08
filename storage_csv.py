import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = {}
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    data[title] = {
                        'rating': float(row['rating']),
                        'year': row['year'],
                        'poster_url': row['poster_url']
                    }
        except FileNotFoundError:
            pass
        return data

    def save_data(self, data):
        with open(self.file_path, mode='w', newline='') as file:
            fieldnames = ['title', 'rating', 'year', 'poster_url']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, info in data.items():
                writer.writerow({
                    'title': title,
                    'rating': info['rating'],
                    'year': info['year'],
                    'poster_url': info['poster_url']
                })

    def list_movies(self):
        return self.load_data()

    def add_movie(self, title, year, rating, poster_url):
        data = self.load_data()
        if title in data:
            print(f"Movie {title} already exists!")
            return
        data[title] = {"year": year, "rating": rating, "poster_url": poster_url}
        self.save_data(data)
        print(f"Movie {title} successfully added")

    def delete_movie(self, title):
        data = self.load_data()
        if title not in data:
            print(f"Movie {title} does not exist!")
            return
        del data[title]
        self.save_data(data)
        print(f"Movie {title} successfully deleted")

    def update_movie(self, title, rating):
        data = self.load_data()
        if title not in data:
            print(f"Movie {title} does not exist!")
            return
        data[title]["rating"] = rating
        self.save_data(data)
        print(f"Rating of movie {title} successfully updated to {rating}")
