import os
import sys

branch = "master"
what = sys.argv[1]

if len(sys.argv) >= 3:
    branch = sys.argv[2]

setup = "python websetup_run.py " + what
if branch is not "master":
    setup += " " + branch

steps = [
    "git clone --recurse-submodules https://github.com/milos85vasic/Apache-Factory-Toolkit.git ./",
    setup
]

for cmd in steps:
    os.system(cmd)
