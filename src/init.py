import logging

import paths


log = logging.getLogger(__name__)


def run() -> bool:
    log.info("Creating the directories")
    for directory in (paths.WIT, paths.IMAGES, paths.INDEX):
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except OSError:
            log.exception("init: Can't create the directories")
            return False
    log.info("Creation of the directories was successful")
    return True

