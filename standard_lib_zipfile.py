from pathlib import Path
from zipfile import ZipFile

#zip = ZipFile("zfile.zip", "w") # create a zipfile object in write mode. zip obj is in current folder

with ZipFile("zfile.zip", "w") as zip:
    # To create a zip file containing all files from folder Module_package
    for path in Path("Module_package").rglob("*.*"):
        zip.write(path)
# To read contents of zip file
with ZipFile("zfile.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("Module_package/sample.txt")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")