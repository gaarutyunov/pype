import logging

from pype.core.command import Command


class Strategy:
    """Class that implements commands handlers"""
    def run(self, command: Command, params: dict[str, str]):
        if hasattr(self, command.name):
            getattr(self, command.name)(command, params)
        else:
            logging.debug("Skipping %s", command.name)
