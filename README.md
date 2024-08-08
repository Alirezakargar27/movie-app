**Movie App**

**Overview**
This project is a comprehensive Movie Application developed as part of a class project. It allows users to manage a collection of movies with features like adding, listing, updating, deleting, and fetching movie data from the OMDb API. Additionally, it supports generating a simple HTML website to display the movie collection and offers multiple storage options, including JSON and CSV.

**Features**
- **CRUD Operations**: Create, Read, Update, Delete movies.
- **Statistics**: Display total count and average rating of movies.
- **Random Movie**: Fetch a random movie from the collection.
- **Search**: Search movies by title.
- **Sort**: List movies sorted by rating.
- **Website Generation**: Generate a static HTML website to display movies.
- **Multiple Storage Options**: Support for JSON and CSV storage formats.

**Technologies and Concepts**
- **Python**: The main programming language used.
- **Requests**: Library for HTTP requests to fetch data from the OMDb API.
- **CSV and JSON**: Python's built-in libraries for handling CSV and JSON data.
- **OOP Principles**: Encapsulation, modularity, and interface segregation.

**File Structure**
- **istorage.py**: Defines the IStorage interface for storage operations.
- **storage_json.py**: Implements the StorageJson class for JSON storage.
- **storage_csv.py**: Implements the StorageCsv class for CSV storage.
- **movie_app.py**: Contains the MovieApp class with the main application logic.
- **main.py**: The entry point of the application.

**Future Enhancements**
- **Database Storage**: Support for databases such as SQLite or PostgreSQL.
- **Web Interface**: Developing a web-based UI using Flask or Django.
- **Improved Error Handling**: Better error handling and user feedback.
