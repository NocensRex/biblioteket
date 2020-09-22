from mediatype import Book, Movie, Music_CD


class Lib():
    def __init__(self):
        self.books = []
        self.movies = []
        self.music_cds = []

    def add_book(self, title, author, page_count, purchase_price, purchase_year):
        self.books.append(Book(title, author, page_count, purchase_price, purchase_year))

    def add_movie(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        self.movies.append(Movie(title, director, length, purchase_price, purchase_year, degree_of_wear))

    def add_cd(self, title, artist, track_count, length, purchase_price):
        self.music_cds.append(Music_CD(title, artist, track_count, length, purchase_price))

    def print_lib(self):
        print('\nBooks:')
        for book in self.books:
            print(book.title)
        print('\nMovies:')
        for movie in self.movies:
            print(movie.title)
        print('\nMusic CDs:')
        for cd in self.music_cds:
            print(cd.title)
