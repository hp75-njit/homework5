from abc import ABC, abstractmethod
from decimal import Decimal
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, input_str: str):
        parts = input_str.split()
        if len(parts) == 0:
            print("Please enter a command.")
            return

        command_name = parts[0]
        command = self.commands.get(command_name)

        try:
            # If the command is 'menu' or 'exit', won't pass numbers
            if command_name in ['menu', 'exit']:
                command.execute()
            # For all other commands
            elif len(parts) == 3:              
                try:
                    a = Decimal(parts[1])
                    b = Decimal(parts[2])
                    command.execute(a, b)
                except ValueError:
                    print("Please enter valid numbers.")
            else:
                print("Please provide two numbers.")
        except KeyError:
            print(f"Unknown command: {command_name}. Type 'menu' for options.")