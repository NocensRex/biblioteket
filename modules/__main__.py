import cmd
import json

from modules.library import Lib


class LibShell(cmd.Cmd):
    # TODO: Write more
    intro = 'Welcome! Write more info here'
    prompt = '->'

    def preloop(self):
        self.my_library = Lib()
        load_data()

    def do_add(self, arg):
        obj = add_media()
        self.my_library.add_media(obj)
        self.my_library.update_prices()
        # b = book, m = movie, c = music cd

        # arg_list = to_list(parse(arg))
        # if arg_list[1] is True:
        #     self.my_library.add_media(arg_list[0])
        #     self.my_library.update_prices()
        # else:
        #     print('You did not give correct amount of data')


    def do_update(self, arg):
        self.my_library.update_prices()

    def do_debug(self, arg):
        'This is a debug option to populate the library with random data'
        self.my_library.add_media(['b', 'd Book', 'f author', 45, 43, 1567])
        self.my_library.add_media(['b', 'a Book', 'g author', 23, 123, 2014])
        self.my_library.add_media(['b', 'h Book', 'b author', 5, 23, 2019])
        self.my_library.add_media(['b', 'b Book', 'm author', 6, 98, 2012])
        self.my_library.add_media(['b', 'i Book', 'd author', 8, 1, 2015])
        self.my_library.add_media(['c', 'g cd', 'l artist', 6, 56, 309])
        self.my_library.add_media(['c', 'w cd', 'd artist', 13, 108, 67])
        self.my_library.add_media(['c', 'x cd', 'n artist', 7, 70, 120])
        self.my_library.add_media(['c', 'x cd', 'n artist', 8, 54, 100])
        self.my_library.add_media(['c', 'x cd', 'n artist', 12, 66, 200])
        self.my_library.add_media(['c', 'j cd', 'j artist', 4, 34, 123])
        self.my_library.add_media(['c', 'n cd', 'a artist', 23, 48, 432])
        self.my_library.add_media(['c', 'n cd', 'a artist', 23, 48, 432])
        self.my_library.add_media(['m', 'good one', 'gustav', 156, 123, 2019, 10])
        self.my_library.add_media(['m', 'decent one', 'davidsson', 120, 230, 2015, 7])
        self.my_library.add_media(['m', 'eehh', 'matsumoto', 99, 98, 2012, 5])
        self.my_library.add_media(['m', 'not good', 'gusten', 56, 43, 2018, 3])
        self.my_library.add_media(['m', 'bad bad', 'god', 66, 666, 2012, 1])

    def do_save(self, arg):
        save_data(self.my_library.to_dict())

    def do_load(self, arg):
        import_data = from_file()
        for elm in import_data:
            exec(elm.rstrip())

    def do_d(self, arg):
        print(vars(self.my_library))

    def do_show(self, arg):
        # all = show all
        self.my_library.show(*parse(arg))

    def do_quit(self, *arg):
        'Exit the Program'
        return True


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


# FIXME: Need to work
def load_data():
    try:
        with open('data/data.json', 'r') as f:
            import_dict = json.load(f)
        return import_dict
    except FileNotFoundError:
        print('No file found')


def to_file(data: Lib):
    data_list = data.media
    with open('data/data.txt', 'w') as f:
        for elm in data_list:
            print(repr(elm))
            f.write(repr(elm) + '\n')


def from_file():
    with open('data/data.txt', 'r') as f:
        data_list = f.readlines()
    return data_list
