import logging

from pype import Command


class Echo(Command):
    logger: logging.Logger | None = None

    def __init__(self, log_level: str = "ERROR"):
        super().__init__("echo")  # echo is the name of the command
        self.log_level = log_level

    def configure(self, **kwargs: str):
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.log_level)
