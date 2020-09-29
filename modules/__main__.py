import cmd
import csv

from modules.library import Lib
from modules.library import Media


class LibShell(cmd.Cmd):
    # TODO: Write more
    intro = 'Welcome! Write more info here'
    prompt = '->'

    def preloop(self):
        self.my_library = Lib()
        self.populate(load_from_csv())
        self.my_library.update_prices()

    def postloop(self):
        save_to_csv(self.my_library.media)

    def do_add(self, arg):
        obj = add_media()
        self.my_library.media.append(Media.create(obj[0], obj[1]))
        self.my_library.update_prices()

    def do_update(self, arg):
        self.my_library.update_prices()

    def do_save(self, arg):
        save_to_csv(self.my_library.media)

    def do_load(self, arg):
        self.populate(load_from_csv())
        self.my_library.update_prices()

    def do_d(self, arg):
        save_to_csv(self.my_library.media)

    def do_d2(self, arg):
        self.populate(load_from_csv())

    def do_show(self, arg):
        self.show(*parse(arg))

    def do_quit(self, *arg):
        'Exit the Program'
        return True

    def populate(self, data):
        for elm in data:
            self.my_library.media.append(Media.create(elm[0], elm[1]))

    def show(self, sort='title'):
        books = []
        movies = []
        cds = []
        if sort == 'title':
            sort_index = 0
        elif sort == 'price':
            sort_index = 1
        for x in self.my_library.media:
            if x.mediatype == 'Book':
                books.append((x.title, x.current_price, x))
            if x.mediatype == 'Movie':
                movies.append((x.title, x.current_price, x))
            if x.mediatype == 'Music_CD':
                cds.append((x.title, x.current_price, x))
        print('\nBooks')
        print('------------')
        print('mediatype, title, creator, purchase_price, current_price, page_count, purchase_year, age')
        books = sorted(books, key=lambda x: x[sort_index])
        for book in books:
            print(book[2])
        print('\nMovies')
        print('------------')
        print('mediatype, title, creator, purchase_price, current_price, length, purchase_year, age, degree_of_wear')
        movies = sorted(movies, key=lambda x: x[sort_index])
        for movie in movies:
            print(movie[2])
        print('\nMusic CDs')
        print('------------')
        print('mediatype, title, creator, purchase_price, current_price, track_count, length')
        cds = sorted(cds, key=lambda x: x[sort_index])
        for cd in cds:
            print(cd[2])


def parse(args):
    print(args)
    return tuple(args.split())


def add_media():
    'Add an media object'
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


def save_to_csv(data):
    with open('data/data.csv', 'w', newline='') as f:
        csv_out = csv.writer(f)
        for row in data:
            csv_out.writerow(row.save())


def load_from_csv():
    with open('data/data.csv', 'r', newline='') as f:
        csv_in = csv.reader(f)
        data = []
        for row in csv_in:
            data.append((row[0], row[1:]))

    return data
