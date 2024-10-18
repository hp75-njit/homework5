import sys
from app.commands import Command


# command for the exit
class ExitCommand(Command):
    def execute(self, a=None, b=None):
        sys.exit("Exiting...")