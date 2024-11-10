from typing import Callable

from .protocols import VCSAdapter

FACTORIES = {}

def register_factory(name):
    def register(factory: Callable[[], VCSAdapter]):
        FACTORIES[name] = factory

    return register


def get_factory(name):
    return FACTORIES[name]
