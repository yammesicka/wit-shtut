import logging
from pathlib import Path
import sys
from typing import cast

import errors
import paths


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def init() -> bool:
    log.info("Creating the directories")
    for directory in (paths.WIT, paths.IMAGES, paths.INDEX):
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except OSError:
            log.exception("init: Can't create the directories")
            return False
    log.info("Creation of the directories was successful")
    return True

#
# def add(path_: str) -> bool:
#     path = Path(path_)
#
#


def main(path: str, *args: str) -> bool:
    if not args:
        raise errors.NoArgumentsError("Must provide arguments for wit command")

    command, *params = args

    if command == "init":
        if params:
            raise errors.NumberOfArgumentsError(f"Expected to get 1 argument, got {len(params)}")
        return init(*params)

    raise errors.CommandNotFoundError()


if __name__ == '__main__':
    main(*sys.argv)
