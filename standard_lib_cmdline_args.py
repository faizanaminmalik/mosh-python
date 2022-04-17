import sys

if len(sys.argv) == 1:
    print("Usage: Need a password argument")
else:
    paswd = sys.argv[1]
    print("Password:", paswd)