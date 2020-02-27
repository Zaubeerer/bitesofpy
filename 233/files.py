from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path('/tmp')
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE, n: int = 3):
    pass