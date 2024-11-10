import logging

from pype.core.command import Command
from pype.core.strategy import Strategy


class Stage:
    """A list of commands to be handled by a Strategy one by one"""

    def __init__(self, name: str, strategy: Strategy, commands: list[Command]):
        """
        :param name: Name of the stage
        :param strategy: Strategy that handles the commands
        :param commands: List of commands to be handled
        """
        self.name = name
        self.strategy = strategy
        self.commands = commands

    def run(self, params: dict[str, str]):
        """
        Run the commands sequentially
        :param params:
        """
        for command in self.commands:
            logging.info("Command %s", command.name)

            if hasattr(self.strategy, f"configure_{command.name}"):
                logging.debug(
                    "%s configuring command %s",
                    type(self.strategy).__name__,
                    command.name,
                )
                getattr(self.strategy, f"configure_{command.name}")(command, **params)

            command.configure(**params)
            self.strategy.run(command, params)
