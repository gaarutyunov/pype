import io
import os

from gitlab import Gitlab

from pype.vcs import VCSAdapter, register_factory


@register_factory("gitlab")
def gitlab_factory() -> VCSAdapter:
    return GitlabAdapter(os.environ.get("GITLAB_URL"), os.environ.get("GITLAB_TOKEN"))


class GitlabAdapter:
    def __init__(self, url: str, token: str):
        self.client = Gitlab(url, token)

    def download(self, repository: str, filename: str, ref: str) -> io.TextIOBase:
        return io.StringIO(self.client.projects.get(repository).files.get(filename, ref=ref).decode().decode("utf-8"))