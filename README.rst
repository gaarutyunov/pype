pype
====

Command
-------

Commands get dispatched when Pipeline is executed. It's required to define a name for the command.
It can also hold some dependencies used by strategies upon execution.
These dependencies should be defined overriding method `configure`, that is executed before dispatching the command.

.. code:: python

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

Strategy
--------

Strategy holds command handlers. A command handler is a class method with the same name as the command.

In addition, a strategy can configure commands or their dependencies.
In that case you need to define a method with prefix `configure_`.

.. code:: python

    from pype import Strategy, Command

    class LoggerStrategy(Strategy):
        def configure_echo(self, cmd: Echo, **kwargs: dict[str, str]):
            cmd.log_level = "INFO"

        def echo(self, cmd: Echo, params: dict[str, str]):
            cmd.logger.debug(params["MESSAGE"])


.. note::
    Strategy `configure_` methods are executed before commands `configure`.
    Usually they are used to define some prerequisites of the command's dependencies.

Pipeline Configuration
----------------------

A Pipeline can be configured using a YAML file.
It can be a local file or a file stored somewhere, e.g. git repository.

.. code:: yaml

    _target_: pype.Pipeline
    stages:
      - _target_: pype.Stage
        name: "examples:logger"
        strategy:
          _target_: examples.logger.LoggerStrategy
        commands:
          - _target_: examples.logger.Echo
            log_level: DEBUG

Running the Pipeline
--------------------

If the pipeline configuration is stored locally, run `pype --local config.yml`.

If it is stored in a repository, run `pype --source github --repository gaarutyunov/pype --filename examples/config.yml --ref main`.
