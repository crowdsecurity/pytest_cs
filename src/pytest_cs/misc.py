import pathlib

import pytest


def lookup_project_repo() -> pathlib.Path:
    """Return the root of the git repository containing the current directory."""
    root = pathlib.Path.cwd()
    while not (root / ".git").exists():
        root = root.parent
        if root == pathlib.Path("/"):
            raise RuntimeError("No git repo found")

    return root


@pytest.fixture(scope="session")
def project_repo() -> pathlib.Path:
    return lookup_project_repo()
