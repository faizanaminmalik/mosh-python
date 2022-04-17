from pathlib import Path

path = Path("Module_package/ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print (path.name)
