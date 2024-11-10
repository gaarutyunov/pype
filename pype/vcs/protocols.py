import io
from typing import Protocol, TypeAlias


class RepositoryFileClient(Protocol):
    def download(self, repository: str, filename: str, ref: str) -> io.TextIOBase: ...


VCSAdapter: TypeAlias = RepositoryFileClient
