import os
from pathlib import Path
import tempfile

import pytest

from wit import init


TEMPDIR = Path(tempfile.gettempdir())


def test_init_creates_folders():
    test_dir = TEMPDIR / 'init_test'
    test_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(test_dir)
    number_of_files_before = len(os.listdir(test_dir))
    init.run()
    number_of_files_after = len(os.listdir(test_dir))
    assert number_of_files_before + 1 == number_of_files_after

