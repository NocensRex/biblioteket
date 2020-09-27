import cmd

from modules.library import Lib


class LibShell(cmd.Cmd):
    # TODO: Write more
    intro = 'Welcome! Write more info here'
    prompt = '->'

    def preloop(self):
        self.my_library = Lib()

    def do_add(self, arg):
        # b = book, m = movie, c = music cd
        arg_list = to_list(parse(arg))
        print(arg_list)
        if arg_list[1] is True:
            self.my_library.add_media(arg_list[0])
            self.my_library.update_prices()
        else:
            print('You did not give correct amount of data')

    def do_update(self, arg):
        self.my_library.update_prices()

    def do_show(self, arg):
        # all = show all
        self.my_library.show()
        print(vars(self.my_library))

    def do_quit(self, *arg):
        'Exit the Program'
        return True


def parse(args):
    return tuple(args.split())


def to_list(args):
    # TODO: Add more to strings
    print(args)
    if args[0] == 'b':
        if len(args) == 6:
            return ([args[0], args[1], args[2], int(args[3]), float(args[4]), int(args[5])], True)
        else:
            return (False, False)
    elif args[0] == 'm':
        if len(args) == 7:
            return ([args[0], args[1], args[2], int(args[3]), float(args[4]), int(args[5]), int(args[6])], True)
        else:
            return (False, False)
    elif args[0] == 'c':
        if len(args) == 6:
            return ([args[0], args[1], args[2], int(args[3]), int(args[4]), float(args[5])], True)
        else:
            return (False, False)
    else:
        print('You did not define what mediatype you wish to add')


def to_json(data):
    pass


def from_json():
    pass
