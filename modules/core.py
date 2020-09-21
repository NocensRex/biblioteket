import cmd


class LibShell(cmd.Cmd):
    intro = "Welcome to this test (type help for more info)"
    prompt = '->'

    def do_add_book(self, arg):
        pass

    def do_add_cd(self, arg):
        pass

    def do_add_movie(self, arg):
        pass

    def do_quit(self, *arg):
        'Exit the Program'
        return True

    def precmd(self, line):
        line = line.lower()
        return line
