from modules.mediatype import Book, Movie, Music_CD
from pandas import DataFrame


class Lib():
    def __init__(self):
        self.books = []
        self.movies = []
        self.music_cds = []

    def add_book(self, title, author, page_count, purchase_price, purchase_year):
        'Add a book to the library'
        self.books.append(Book(title, author, page_count, purchase_price, purchase_year))

    def add_movie(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        self.movies.append(Movie(title, director, length, purchase_price, purchase_year, degree_of_wear))

    def add_cd(self, title, artist, track_count, length, purchase_price):
        self.music_cds.append(Music_CD(title, artist, track_count, length, purchase_price))

    # FIXME: Do not loop everything. Only that which is needed. arg eg (self, obj)
    def update_current_value(self):
        for obj in self.books:
            obj.set_current_value()
        for obj in self.movies:
            obj.set_current_value()
        for obj in self.music_cds:
            obj.set_current_value(len(self.music_cds))

    # FIXME: Do NOT use pandas
    def print_lib(self):
        print('\nBooks:')
        temp = []
        for book in self.books:
            temp.append((book.title,
                        book.author,
                        book.page_count,
                        book.purchase_price,
                        book.current_value,
                        book.purchase_year))
        df = DataFrame(temp, columns=['Title',
                                      'Author',
                                      'Page Count',
                                      'Purchase Price',
                                      'Current Value',
                                      'Purchase Year'])
        df = df.set_index('Title')
        print(df)
        print('\nMovies:')
        temp = []
        for movie in self.movies:
            temp.append((movie.title,
                        movie.director,
                        movie.length,
                        movie.purchase_price,
                        movie.current_value,
                        movie.purchase_year,
                        movie.degree_of_wear))
        df = DataFrame(temp, columns=['Title',
                                      'Director',
                                      'Length',
                                      'Purchase Price',
                                      'Current Value',
                                      'Purchase Year',
                                      'Degree of wear'])
        df = df.set_index('Title')
        print(df)
        print('\nMusic CDs:')
        temp = []
        for cd in self.music_cds:
            temp.append((cd.title,
                        cd.artist,
                        cd.track_count,
                        cd.length,
                        cd.purchase_price,
                        cd.current_value))
        df = DataFrame(temp, columns=['Title',
                                      'Artist',
                                      'Track Count',
                                      'Length',
                                      'Purchase Price',
                                      'Current Value'])
        df = df.set_index('Title')
        print(df)
