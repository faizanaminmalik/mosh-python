from pathlib import Path
from time import ctime
import shutil
path = Path("Module_package/sample.txt")

print(path.exists())
# path.rename("new.py")
# path.unlink()
print(path.stat())
print(ctime(path.stat().st_ctime))

# will show contents of file
print(path.read_text())
path.write_text("hello i am sample")

print("*******Copy file to another file**************")
source = Path("Module_package/sample.txt")
target = Path("Module_package/sample1.txt")

target.write_text(source.read_text())

#easy way to make use of shutil (import shutil also)
shutil.copy(source, target)