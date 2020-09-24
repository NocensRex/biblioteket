from modules.mediatype import Book, Movie, Music_CD
from modules.indexing import indexing


class Lib():
    def __init__(self):
        self.books = []
        self.movies = []
        self.music_cds = []

    def add_book(self, title, author, page_count, purchase_price, purchase_year):
        'Add a book to the library'
        self.books.append(Book(title, author, int(page_count), float(purchase_price), int(purchase_year)))
        self.update_current_value('book')

    def add_movie(self, title, director, length, purchase_price, purchase_year, degree_of_wear):
        'Add a movie to the library'
        self.movies.append(Movie(title, director, int(length), float(purchase_price), int(purchase_year), int(degree_of_wear)))
        self.update_current_value('movie')

    def add_cd(self, title, artist, track_count, length, purchase_price):
        'Add a music cd to the library'
        self.music_cds.append(Music_CD(title, artist, int(track_count), int(length), float(purchase_price)))
        self.update_current_value('cd')

    # FIXME: Do not loop everything. Only that which is needed. arg eg (self, obj)
    def update_current_value(self, obj):
        'Updates the current value of an object'
        if obj == 'book':
            for obj in self.books:
                obj.set_current_value()
        elif obj == 'movie':
            for obj in self.movies:
                obj.set_current_value()
        elif obj == 'cd':
            for obj in self.music_cds:
                # FIXME: The amount is not calculated correct. It should be similar cds not all cds.
                obj.set_current_value(len(self.music_cds))

    def show_all(self, order='title'):
        'This will show all items in library. Default sort is by title. Argument price to sort by current value'
        unsorted_list = []
        for book in self.books:
            unsorted_list.append(book.get_all())
        sorted_list = indexing(unsorted_list, order)
        print('Books:')
        for book in sorted_list:
            print(book)
        unsorted_list = []
        for movie in self.movies:
            unsorted_list.append(movie.get_all())
        sorted_list = indexing(unsorted_list, order)
        print('Movies:')
        for movie in sorted_list:
            print(movie)
        unsorted_list = []
        for cd in self.music_cds:
            unsorted_list.append(cd.get_all())
        sorted_list = indexing(unsorted_list, order)
        print('Music CDs:')
        for cd in sorted_list:
            print(cd)
            # print(f'Title: {book.get_all()[0]}, Purchase Price: {book.get_all()[3]}, Current Value: {book.get_all()[5]},
            # Author: {book.get_all()[1]}, Page Count: {book.get_all()[2]}, Purchase Year: {book.get_all()[4]}')
