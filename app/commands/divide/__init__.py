import sys
from app.commands import Command
from decimal import Decimal

# command for the divsion
class DivideCommand(Command):

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        else:
            print(f"Result: {a / b}")
