from pathlib import Path

from typing import NamedTuple


class Paths(NamedTuple):
    cwd: Path
    wit: Path
    images: Path
    staging: Path


def get():
    cwd = Path.cwd()

    return Paths(
        cwd=cwd,
        wit=cwd / ".wit",
        images=cwd / ".wit" / "images",
        staging=cwd / ".wit" / "staging_area",
    )
