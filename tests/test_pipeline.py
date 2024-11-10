import pathlib
import sys

from click.testing import CliRunner

from pype.cli import cli


def test_pipeline_local(caplog):
    runner = CliRunner()
    root_path = pathlib.Path(__file__).parent.parent
    config_path = root_path / 'examples/logger/config.yml'
    msg = "test message"
    result = runner.invoke(cli, ['--local', str(config_path)], env={
        "MESSAGE": msg,
        "LOG_LEVEL": "INFO"
    })
    assert result.exit_code == 0
    assert msg in caplog.messages