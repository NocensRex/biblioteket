import cmd
import lib_class


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

    def do_show_all(self, arg):
        'Print out the entire content of the library'
        self.my_library.print_lib()

    def do_debug(self, arg):
        'This is a debug option to populate the library with random data'
        self.my_library.add_book('freg', 'derg', 23, 123, 2014)
        self.my_library.add_book('sdf', 'fsa', 45, 43, 567)
        self.my_library.add_book('hyt', 'bgty', 5, 23, 2019)
        self.my_library.add_book('dswei', 'mnbv', 6, 98, 2012)
        self.my_library.add_book('saser', 'dzxrt', 8, 1, 2015)
        self.my_library.add_cd('wololo', 'derpington', 13, 108, 67)
        self.my_library.add_cd('gtre', 'lpoi', 6, 56, 309)
        self.my_library.add_cd('xcvpoi', 'njiuugh', 7, 7, 7)
        self.my_library.add_cd('johan', 'david', 4, 34, 123)
        self.my_library.add_cd('nicklas', 'magnis', 23, 48, 432)
        self.my_library.add_movie('good one', 'gustav', 156, 123, 2019, 10)
        self.my_library.add_movie('decent one', 'davidsson', 120, 230, 2015, 7)
        self.my_library.add_movie('eehh', 'matsumoto', 99, 98, 2012, 5)
        self.my_library.add_movie('not good', 'gusten', 56, 43, 2018, 3)
        self.my_library.add_movie('bad bad', 'god', 66, 666, 2012, 1)

    def do_quit(self, *arg):
        'Exit the Program'
        return True

    def precmd(self, line):
        line = line.lower()
        return line


def parse(arg):
    return tuple(arg.split())
