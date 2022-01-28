import os, time

path = r"D:\Sample"
now = time.time()

for filename in os.listdir(path):
    # if os.stat(os.path.join(path, filename)).st_mtime < now - 7 * 86400:
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))

import os
from pathlib import Path
from zipfile import ZipFile


DOWNLOAD_DIR = Path("D:\Sample")
ZIPPED_FILE_DIR = Path("D:\Sample")


def get_list_of_all_folders(download_dir: Path):
    return [f for f in download_dir.iterdir() if download_dir.is_dir()]


def zip_files():
    folder_list = get_list_of_all_folders(DOWNLOAD_DIR)
    with ZipFile(ZIPPED_FILE_DIR / "my_zip.zip", "w") as zip:
        # writing each file one by one
        for folder in folder_list:
            zip.write(folder)


zip_files()
