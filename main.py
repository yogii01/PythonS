import os, datetime

path = 'D:\Sample'
os.chdir(path)
files= os.getcwd()
files = os.listdir(files)
files = sorted(files,key=os.path.getmtime)
latest = files.reverse()

for file in files[5:]:
    os.remove(os.path.join(path, file))

for file in files[:5]:
    print(file)





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
