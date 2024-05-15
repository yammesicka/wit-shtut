class WitError(Exception):
    pass


class NoArgumentsError(WitError):
    pass


class CommandNotFoundError(WitError):
    pass


class NumberOfArgumentsError(WitError):
    pass
