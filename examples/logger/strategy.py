from .commands import Echo
from pype import Strategy


class LoggerStrategy(Strategy):
    def configure_echo(self, cmd: Echo, **kwargs: dict[str, str]):
        cmd.log_level = "INFO"

    def echo(self, cmd: Echo, params: dict[str, str]):
        cmd.logger.info(params["MESSAGE"])