import logging
import sys

from pype.core.stage import Stage


class Pipeline:
    """Entrypoint for the pipeline to be executed"""

    def __init__(self, stages: list[Stage]):
        """
        :param stages: list of stages to be run inside pipeline
        """
        self.stages = stages

    def run(self, params: dict[str, str]):
        """
        Run stages sequentially
        :param params: all available parameters
        """
        logging.basicConfig(stream=sys.stdout, level=params.get("LOG_LEVEL", "ERROR"))

        for stage in self.stages:
            logging.info("Stage %s", stage.name)
            stage.run(params)
