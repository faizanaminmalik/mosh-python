from pathlib import Path

path = Path("Module_package")
#print (path.exists())
#path.mkdir()
#path.rmdir()
#path.rename("dir")

print(path.iterdir()) # returns generator object

# will print all contents of directory
for p in path.iterdir():
    print(p)
# will print all contents of directory
print([p for p in path.iterdir()])

#will only print directory
print([p for p in path.iterdir() if p.is_dir()])

# To use expressions we use glob
path.glob("*.py")

for p in path.glob("*.py"):
    print(p)
# We can use comprehension
print([p for p in path.glob("*.py")])

# To search recursively
print([p for p in path.glob("**/*.py")])

# To search recursively by using rglob() method
print([p for p in path.rglob("*.py")])