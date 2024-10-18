"""Tests to cover operations"""
from decimal import Decimal
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands import CommandHandler

def assert_equal(actual, expected, description=""):
    if actual == expected:
        print(f"PASS: {description}")
    else:
        print(f"FAIL: {description} - Expected: {expected}, but got: {actual}")
def test_add_command():
    add_cmd = AddCommand()
    result = add_cmd.execute(Decimal('10'), Decimal('5'))
    assert_equal(result, "Result: 15", "Add Command Test")
def test_subtract_command():
    subtract_cmd = SubtractCommand()
    result = subtract_cmd.execute(Decimal('10'), Decimal('5'))
    assert_equal(result, "Result: 5", "Subtract Command Test")
def test_multiply_command():
    multiply_cmd = MultiplyCommand()
    result = multiply_cmd.execute(Decimal('10'), Decimal('5'))
    assert_equal(result, "Result: 50", "Multiply Command Test")
def test_divide_command():
    divide_cmd = DivideCommand()

    # Test valid division
    result = divide_cmd.execute(Decimal('10'), Decimal('5'))
    assert_equal(result, "Result: 2", "Divide Command Test (Valid)")
def test_command_handler():
    handler = CommandHandler()
    handler.register_command("add", AddCommand())
    handler.register_command("subtract", SubtractCommand())
    handler.register_command("multiply", MultiplyCommand())
    handler.register_command("divide", DivideCommand())
    # Test addition
    result = handler.execute_command("add 10 5")
    assert_equal(result, "Result: 15", "CommandHandler Add Command Test")
    # Test subtraction
    result = handler.execute_command("subtract 10 5")
    assert_equal(result, "Result: 5", "CommandHandler Subtract Command Test")
    # Test multiplication
    result = handler.execute_command("multiply 10 5")
    assert_equal(result, "Result: 50", "CommandHandler Multiply Command Test")
    # Test division
    result = handler.execute_command("divide 10 5")
    assert_equal(result, "Result: 2", "CommandHandler Divide Command Test (Valid)")
    # Test unknown command
    result = handler.execute_command("unknown")
    assert_equal(result, "Unknown command: unknown. Type 'menu' for options.", "CommandHandler Unknown Command Test")
def run_tests():
    test_add_command()
    test_subtract_command()
    test_multiply_command()
    test_divide_command()
    test_command_handler()
if __name__ == '__main__':
    run_tests()
