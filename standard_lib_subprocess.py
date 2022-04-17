import subprocess

#completed = subprocess.run(["ls", "-la"], capture_output=True, text=True)
completed = subprocess.run(["python", "other.py"], capture_output=True, text=True) # u can add check=True to automatically raise exception if returncode is non zero
# The python script invoked above will be in diff memory locations and will not share any data/ variables
print("args", completed.args)
print("returncode", completed.returncode) # Any non-zero code returns an error
print("stderr", completed.stderr)
print("stdout", completed.stdout)