import cmd
import modules.lib_class as lib_class
from modules.other import read_from_file, write_to_json, read_from_custom_file


class LibShell(cmd.Cmd):
    intro = "Welcome to this test (type help for more info)"
    prompt = '->'

    def preloop(self):
        self.my_library = lib_class.Lib()

    def do_add_book(self, arg):
        'Add a book to the library\nArguments: title author page_count purchase_price purchase_year'
        self.my_library.add_book(*parse(arg))

    def do_add_cd(self, arg):
        'Add a Music CD to the library\nArguments: title artist track_count length purchase_price'
        self.my_library.add_cd(*parse(arg))

    def do_add_movie(self, arg):
        'Add a Movie to the library\nArguments: title director length purchase_price purchase_year degree_of_wear'
        self.my_library.add_movie(*parse(arg))

    def do_update_value(self, arg):
        'Updates all current prices'
        self.my_library.update_current_value()

    def do_custom(self, arg):
        read_from_custom_file(*parse(arg))

    def do_save(self, arg):
        'This will save the data in library to files'
        write_to_json(self.my_library)

    def do_load(self, arg):
        'Load data from the save file'
        self.populate_from_json()

    def do_show_all(self, arg):
        'Print out the entire content of the library'
        self.my_library.show_all(*parse(arg))

    def do_debug(self, arg):
        'This is a debug option to populate the library with random data'
        self.my_library.add_book('a Book', 'g author', 23, 123, 2014)
        self.my_library.add_book('d Book', 'f author', 45, 43, 567)
        self.my_library.add_book('h Book', 'b author', 5, 23, 2019)
        self.my_library.add_book('b Book', 'm author', 6, 98, 2012)
        self.my_library.add_book('i Book', 'd author', 8, 1, 2015)
        self.my_library.add_cd('w cd', 'd artist', 13, 108, 67)
        self.my_library.add_cd('g cd', 'l artist', 6, 56, 309)
        self.my_library.add_cd('x cd', 'n artist', 7, 7, 7)
        self.my_library.add_cd('x cd', 'n artist', 7, 7, 7)
        self.my_library.add_cd('x cd', 'n artist', 7, 7, 7)
        self.my_library.add_cd('j cd', 'j artist', 4, 34, 123)
        self.my_library.add_cd('n cd', 'a artist', 23, 48, 432)
        self.my_library.add_cd('n cd', 'a artist', 23, 48, 432)
        self.my_library.add_movie('good one', 'gustav', 156, 123, 2019, 10)
        self.my_library.add_movie('decent one', 'davidsson', 120, 230, 2015, 7)
        self.my_library.add_movie('eehh', 'matsumoto', 99, 98, 2012, 5)
        self.my_library.add_movie('not good', 'gusten', 56, 43, 2018, 3)
        self.my_library.add_movie('bad bad', 'god', 66, 666, 2012, 1)

    def do_quit(self, *arg):
        'Exit the Program'
        return True

    def populate_from_json(self):
        'This function populates the library'
        data = read_from_file()
        for key in data:
            for row in data[key]:
                if key == 'books':
                    self.my_library.add_book(row['title'],
                                             row['author'],
                                             row['page_count'],
                                             row['purchase_price'],
                                             row['purchase_year'])
                elif key == 'movies':
                    self.my_library.add_movie(row['title'],
                                              row['director'],
                                              row['length'],
                                              row['purchase_price'],
                                              row['purchase_year'],
                                              row['degree_of_wear'])
                elif key == 'music_cds':
                    self.my_library.add_cd(row['title'],
                                           row['artist'],
                                           row['track_count'],
                                           row['length'],
                                           row['purchase_price'])
        self.my_library.update_current_value('book')
        self.my_library.update_current_value('movie')
        self.my_library.update_current_value('cd')

    def precmd(self, line):
        line = line.lower()
        return line


def parse(arg):
    return tuple(arg.split())
