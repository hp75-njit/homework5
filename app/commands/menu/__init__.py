import sys
from app.commands import Command
from decimal import Decimal

# command for the display
class MenuCommand(Command):
    def execute(self, a=None, b=None):
        print("Available commands: add [a] [b], subtract [a] [b], multiply [a] [b], divide [a] [b], menu, exit")
