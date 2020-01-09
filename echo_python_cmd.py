import os
import sys
import subprocess

if __name__ == '__main__':
    steps = [
        "mkdir Toolkit",
        "git clone --recurse-submodules https://github.com/milos85vasic/Apache-Factory-Toolkit.git ./Toolkit",
    ]

    for cmd in steps:
        os.system(cmd)

    from Toolkit.commands import get_python_cmd
    python_cmd = get_python_cmd()
    print(python_cmd)

    steps = [
        "rm -rf ./Toolkit",
        "rm -f " + os.path.basename(__file__)
    ]

    for cmd in steps:
        os.system(cmd)