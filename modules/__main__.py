import cmd
import json

from modules.library import Lib


class LibShell(cmd.Cmd):
    # TODO: Write more
    intro = 'Welcome! Write more info here'
    prompt = '->'

    def preloop(self):
        self.my_library = Lib()
        self.populate_from_json()

    def postloop(self):
        save_data(self.my_library.to_dict())

    def do_add(self, arg):
        obj = add_media()
        self.my_library.add_media(obj)
        self.my_library.update_prices()

    def do_update(self, arg):
        self.my_library.update_prices()

    def do_save(self, arg):
        save_data(self.my_library.to_dict())

    def do_load(self, arg):
        self.populate_from_json()
        self.my_library.update_prices()

    def do_d(self, arg):
        print(vars(self.my_library))

    def do_show(self, arg):
        self.my_library.show(*parse(arg))

    def do_quit(self, *arg):
        'Exit the Program'
        return True

    def populate_from_json(self):
        'This function populates the library'
        data = load_data()
        for key in data:
            for row in data[key]:
                if key == 'books':
                    self.my_library.add_media(['b',
                                              row['title'],
                                              row['creator'],
                                              row['page_count'],
                                              row['purchase_price'],
                                              row['purchase_year']])
                elif key == 'movies':
                    self.my_library.add_media(['m',
                                              row['title'],
                                              row['creator'],
                                              row['length'],
                                              row['purchase_price'],
                                              row['purchase_year'],
                                              row['degree_of_wear']])
                elif key == 'music_cds':
                    self.my_library.add_media(['c',
                                              row['title'],
                                              row['creator'],
                                              row['track_count'],
                                              row['length'],
                                              row['purchase_price']])


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
        return ['b', title, author, page_count, purchase_price, purchase_year]
    elif choice == 2:
        print('\nAdding a movie')
        title = input('Title: ')
        director = input('Director: ')
        length = int(input('Length in minutes: '))
        purchase_price = float(input('Purchase Price: '))
        purchase_year = int(input('Purchase Year: '))
        degree_of_wear = int(input('Degree of wear (on a scale from 1 to 10): '))
        return ['m', title, director, length, purchase_price, purchase_year, degree_of_wear]
    elif choice == 3:
        print('\nAdding a music cd')
        title = input('Title: ')
        artist = input('Artist: ')
        track_count = int(input('Track Count: '))
        length = int(input('Length in minutes: '))
        purchase_price = float(input('Purchase Price: '))
        return ['c', title, artist, track_count, length, purchase_price]

    else:
        print('You did not give an acceptable answer')


def save_data(data):
    with open('data/data.json', 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, sort_keys=True)


def load_data():
    try:
        with open('data/data.json', 'r') as f:
            import_dict = json.load(f)
        return import_dict
    except FileNotFoundError:
        print('No file found')


# FIXME: Redundant code
def to_file(data: Lib):
    data_list = data.media
    with open('data/data.txt', 'w') as f:
        for elm in data_list:
            print(repr(elm))
            f.write(repr(elm) + '\n')


# FIXME: Redundant code
def from_file():
    with open('data/data.txt', 'r') as f:
        data_list = f.readlines()
    return data_list
