import os
import sys
import subprocess

def get_python_cmd():
    pythons = ["python", "python3", "python2"]
    for item in pythons:
        result, _ = subprocess.Popen(["which", item], stdout=subprocess.PIPE).communicate()
        lines = result.splitlines(keepends=False)
        for line in lines:
            utf_line = line.decode('UTF-8')
            if not "no " + item in utf_line:
                return item
    return "python"


branch = "master"
what = sys.argv[1]

if len(sys.argv) >= 3:
    branch = sys.argv[2]

setup = get_python_cmd() + " ./Toolkit/websetup_run.py " + what
if branch is not "master":
    setup += " " + branch

steps = [
    "mkdir Toolkit",
    "git clone --recurse-submodules https://github.com/milos85vasic/Apache-Factory-Toolkit.git ./Toolkit",
    setup,
    "rm -rf ./Toolkit",
    "rm -f " + os.path.basename(__file__)
]

for cmd in steps:
    os.system(cmd)
