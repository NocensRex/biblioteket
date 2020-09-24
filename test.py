import cmd


class TestShell(cmd.Cmd):
    intro = 'This is a test shell'
    prompt = '->'

    def do_asd(self, arg):
        print('Working!')
        print(arg)
        print(type(arg))
        print(parse(arg))
        print(type(parse(arg)))
        print(*parse(arg))

    def do_quit(self, arg):
        print('Bye!')
        return True


def parse(arg):
    return tuple(arg.split())


if __name__ == '__main__':
    TestShell().cmdloop()
