import os
from typing import Any

import click
import yaml

from pype import Pipeline
from pype.registry import REGISTRY
from pype.vcs import get_factory, RepositoryFileClient


@click.command()
@click.option("-s", "--source", help="Configuration remote source")
@click.option("-l", "--local", type=click.File(lazy=True), help="Path to local configuration file")
@click.option("-p", "--repository", type=str, help="Repository full name")
@click.option("-r", "--ref", type=str, help="Reference (branch or tag)")
@click.option("-f", "--file", type=str, help="Config file name")
@click.option("--dry-run", type=bool)
def cli(source, local, repository, ref, file, dry_run):
    if local:
        config = yaml.safe_load(local)
    elif repository and ref and file:
        client = get_factory(source)()
        config = get_config_file(client, repository=repository, filename=file, ref=ref)
    else:
        raise Exception("either local or remote config must be specified")

    pipe: Pipeline = REGISTRY.get_from_params(**config)

    if dry_run:
        print(pipe)
    else:
        pipe.run(os.environ.copy())


def get_config_file(client: RepositoryFileClient, **kwargs: str) -> dict[str, Any]:
    return yaml.safe_load(client.download(**kwargs))
