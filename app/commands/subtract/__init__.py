import sys
from app.commands import Command
from decimal import Decimal

# command for the subtraction
class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
         print(f"Result: {a - b}")
