import io
import os

from github import Github, Auth
from github.Consts import DEFAULT_BASE_URL

from pype.vcs import VCSAdapter, register_factory


@register_factory("github")
def github_factory() -> VCSAdapter:
    return GithubAdapter(
        os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_URL", DEFAULT_BASE_URL)
    )


class GithubAdapter:
    def __init__(self, token: str, url: str = DEFAULT_BASE_URL):
        self.client = Github(auth=Auth.Token(token), base_url=url)

    def download(self, repository: str, filename: str, ref: str) -> io.TextIOBase:
        return io.StringIO(
            self.client.get_repo(repository)
            .get_contents(filename, ref=ref)
            .decoded_content.decode("utf-8")
        )
