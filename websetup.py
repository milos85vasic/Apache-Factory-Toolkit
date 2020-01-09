import os
import sys
import subprocess

if __name__ == '__main__':
    exists = True
    steps = []
    if not os.path.exists("Toolkit"):
        exists = False
        steps.extend(
            [
                "mkdir Toolkit",
                "git clone --recurse-submodules https://github.com/milos85vasic/Apache-Factory-Toolkit.git ./Toolkit",
            ]
        )

    for cmd in steps:
        os.system(cmd)

    branch = "master"
    what = sys.argv[1]

    if len(sys.argv) >= 3:
        branch = sys.argv[2]

    from Toolkit.commands import get_python_cmd
    python_cmd = get_python_cmd()
    setup = python_cmd + " ./Toolkit/websetup_run.py " + what
    if branch is not "master":
        setup += " " + branch

    steps = [
        setup
    ]

    if not exists:
        steps.extend(
            [
                "rm -rf ./Toolkit",
                "rm -f " + os.path.basename(__file__)
            ]
        )

    for cmd in steps:
        os.system(cmd)