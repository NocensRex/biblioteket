from mediatype import Book, Movie, Music_CD
from pandas import DataFrame


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
        temp = []
        for book in self.books:
            temp.append((book.title, book.author, book.page_count, book.purchase_price, book.purchase_year))
        df = DataFrame(temp, columns=['Title', 'Author', 'Page Count', 'Purchase Price', 'Purchase Year'])
        df = df.set_index('Title')
        print(df)
        print('\nMovies:')
        temp = []
        for movie in self.movies:
            temp.append((movie.title, movie.director, movie.length, movie.purchase_price, movie.purchase_year, movie.degree_of_wear))
        df = DataFrame(temp, columns=['Title', 'Director', 'Length', 'Purchase Price', 'Purchase Year', 'Degree of wear'])
        df = df.set_index('Title')
        print(df)
        print('\nMusic CDs:')
        temp = []
        for cd in self.music_cds:
            temp.append((cd.title, cd.artist, cd.track_count, cd.length, cd.purchase_price))
        df = DataFrame(temp, columns=['Title', 'Artist', 'Track Count', 'Length', 'Purchase Price'])
        df = df.set_index('Title')
        print(df)
