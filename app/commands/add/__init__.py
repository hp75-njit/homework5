import sys
from app.commands import Command
from decimal import Decimal

# command for the addition
class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        print(f"Result: {a + b}")
