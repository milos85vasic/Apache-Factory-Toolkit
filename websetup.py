import os
import sys

branch = "master"
what = sys.argv[1]

if len(sys.argv) >= 3:
    branch = sys.argv[2]

setup = "python ./Toolkit/websetup_run.py " + what
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
