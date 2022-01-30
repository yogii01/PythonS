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





import zipfile
import os

working_folder = 'D:\Sample'

files = os.listdir(working_folder)


ZipFile = zipfile.ZipFile("python.zip", "w" )

for a in files:
    ZipFile.write(os.path.basename(a), compress_type=zipfile.ZIP_DEFLATED)
ZipFile.close()
