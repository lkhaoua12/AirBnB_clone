#!/usr/bin/python3
""" console module entry """


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """Exit the console using Ctrl+D (EOF)"""

        print()
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
