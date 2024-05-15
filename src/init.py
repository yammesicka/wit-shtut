import logging

from paths import get as get_paths


log = logging.getLogger(__name__)


def run() -> bool:
    log.info("Creating the directories")
    paths = get_paths()
    
    for directory in (paths.wit, paths.images, paths.staging):
        log.debug(f"Creating {directory}")
        try:
            directory.mkdir(parents=True, exist_ok=True)
            print(directory)
        except OSError:
            log.exception("init: Can't create the directories")
            return False
    log.info("Creation of the directories was successful")
    return True

