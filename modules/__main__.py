import cmd

from modules.library import Lib
from modules.library import Media
from modules.utils import load_from_csv, save_to_csv, fixed_string


class LibShell(cmd.Cmd):
    intro = '''
    Library Register V.1
    With this software all your indexing problems are fixed.
    If you need help type "help" for all the commands.
    You can also typ "help introduction" for help on how to use me.
    '''
    prompt = '->'

    def preloop(self):
        self.my_library = Lib()
        self.populate(load_from_csv())
        self.my_library.update_prices()

    def postloop(self):
        save_to_csv(self.my_library.media)

    def do_add(self, arg):
        'This will add a media object to the library.'
        obj = add_media()
        self.my_library.media.append(Media.create(obj[0], obj[1]))
        self.my_library.update_prices()

    def do_save(self, arg):
        'Manually save the data to "data/data.csv"'
        save_to_csv(self.my_library.media)

    def do_load(self, arg):
        'Manually load the data from "data/data.csv"'
        self.populate(load_from_csv())
        self.my_library.update_prices()

    def do_show(self, arg):
        '''
        This will show all the objects in the library
        Standard sort is by title, if you want to sort by
        price type "show price"
        '''
        self.show(*parse(arg))

    def do_quit(self, *arg):
        'Exit the Program'
        return True

    def help_introduction(self):
        print('''
        Hi and welcome to this introduction

        To begin with try and type "show", with this command
        you will get a view of all the data in the library sorted
        by title. If you want to sort by price type "show price"

        If you want to add new media objects type "add"
        and then chose the the media object you want to add
        after that just type in what the prompt tells you.
        ''')

    def populate(self, data):
        """Populates the library with objects from a list

        Args:
            data (list): list of tuples
        """
        for elm in data:
            self.my_library.media.append(Media.create(elm[0], elm[1]))

    def show(self, sort='title'):
        """This will sort and present the data in library

        Args:
            sort (str, optional): decides by what value to sort after. Defaults to 'title'.
        """
        books = []
        movies = []
        cds = []
        if sort == 'title':
            sort_index = 0
        elif sort == 'price':
            sort_index = 1
        for elm in self.my_library.media:
            if elm.mediatype == 'Book':
                books.append((elm.title, elm.current_price, elm))
            if elm.mediatype == 'Movie':
                movies.append((elm.title, elm.current_price, elm))
            if elm.mediatype == 'Music_CD':
                cds.append((elm.title, elm.current_price, elm))
        print('\nBooks')
        print('------------')
        print(''
              + fixed_string('Title', 29).ljust(30)
              + fixed_string('Author', 29).rjust(30)
              + fixed_string('Current Price', 15).rjust(16)
              + fixed_string('Purchase Price', 15).rjust(16)
              + fixed_string('Page Count', 11).rjust(12)
              + fixed_string('Purchase Year', 14).rjust(15))
        books = sorted(books, key=lambda x: x[sort_index])
        for book in books:
            print(book[2])
        print('\nMovies')
        print('------------')
        print(''
              + fixed_string('Title', 29).ljust(30)
              + fixed_string('Director', 29).rjust(30)
              + fixed_string('Current Price', 15).rjust(16)
              + fixed_string('Purchase Price', 15).rjust(16)
              + fixed_string('Length(minuts)', 15).rjust(16)
              + fixed_string('Purchase Year', 14).rjust(15)
              + fixed_string('Degree of wear', 15).rjust(16))
        movies = sorted(movies, key=lambda x: x[sort_index])
        for movie in movies:
            print(movie[2])
        print('\nMusic CDs')
        print('------------')
        print(''
              + fixed_string('Title', 29).ljust(30)
              + fixed_string('Artist', 29).rjust(30)
              + fixed_string('Current Price', 15).rjust(16)
              + fixed_string('Purchase Price', 15).rjust(16)
              + fixed_string('Track Count', 12).rjust(13)
              + fixed_string('Length(minutes)', 16).rjust(17))
        cds = sorted(cds, key=lambda x: x[sort_index])
        for cd in cds:
            print(cd[2])


def parse(args):
    """Convert a series of zero or more numbers to an argument tuple

    Args:
        args (str): string with arguments (cmd.Cmd module type)

    Returns:
        tuple: tuple of arguments
    """
    print(args)
    return tuple(args.split())


def add_media():
    """Info to be used to create instance of object

    Returns:
        tuple: tuple with identifier and parameters
    """
    print(
        '''What do you want to add
        1. Book
        2. Movie
        3. Music CD''')
    choice = int(input('Make your choice: '))
    if choice == 1:
        print('\nAdding a Book')
        title = input('Title: ')
        author = input('Author: ')
        page_count = int(input('Page Count: '))
        purchase_price = float(input('Purchase Price: '))
        purchase_year = int(input('Purchase Year: '))
        return ('book', [title, author, page_count, purchase_price, purchase_year])
    elif choice == 2:
        print('\nAdding a movie')
        title = input('Title: ')
        director = input('Director: ')
        length = int(input('Length in minutes: '))
        purchase_price = float(input('Purchase Price: '))
        purchase_year = int(input('Purchase Year: '))
        degree_of_wear = int(input('Degree of wear (on a scale from 1 to 10): '))
        return ('movie', [title, director, length, purchase_price, purchase_year, degree_of_wear])
    elif choice == 3:
        print('\nAdding a music cd')
        title = input('Title: ')
        artist = input('Artist: ')
        track_count = int(input('Track Count: '))
        length = int(input('Length in minutes: '))
        purchase_price = float(input('Purchase Price: '))
        return ('cd', [title, artist, track_count, length, purchase_price])

    else:
        print('You did not give an acceptable answer')
