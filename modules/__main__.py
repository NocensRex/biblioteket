import cmd

from modules.library_class import Lib


class LibShell(cmd.Cmd):
    # TODO: Write more
    intro = 'Welcome! Write more info here'
    prompt = '->'

    def preloop(self):
        self.my_library = Lib()

    def do_add(self, arg):
        # b = book, m = movie, c = music cd
        self.my_library.add_media(to_list(parse(arg)))

    def do_show(self, arg):
        # all = show all
        self.my_library.show()

    def do_quit(self, *arg):
        'Exit the Program'
        return True


def parse(args):
    return tuple(args.split())


def to_list(args):
    # TODO: Add more to strings
    if args[0] == 'b':
        if len(args) == 6:
            return [args[0], args[1], args[2], int(args[3]), float(args[4]), int(args[5])]
        else:
            print('You did not give correct amount of data')
    elif args[0] == 'm':
        print('pass')
        if len(args) == 7:
            return [args[0], args[1], args[2], int(args[3]), float(args[4]), int(args[5]), int(args[6])]
        else:
            print('You did not give correct amount of data')
    elif args[0] == 'c':
        print('pass')
        if len(args) == 6:
            return [args[0], args[1], args[2], int(args[3]), int(args[4]), float(args[5])]
        else:
            print('You did not give correct amount of data')
    else:
        print('You did not define what mediatype you wish to add')
