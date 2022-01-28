import os, time

path = "D:\Sample"
now = time.time()

for filename in os.listdir(path):
    filestamp = os.stat(os.path.join(path, filename)).st_mtime
    filecompare = now - 7 * 86400
    if  filestamp < filecompare:
        os.remove(os.path.join(path, filename))
        print(filename)
