#!/usr/bin/python3
"""
console 0.0.1
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """comand interpreter file"""
    prompt = "(hbhb)"
    def do_quit(self, args):
        """quit the program"""
        return True
    def do_EOF(self, args):
        """end of file"""
        return True
    def emptyline(self):
        """empty line"""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
