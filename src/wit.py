import logging
import sys

import init
import errors


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


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
        return init.run(*params)

    raise errors.CommandNotFoundError()


if __name__ == '__main__':
    main(*sys.argv)
