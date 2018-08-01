import sys
from commands import *
from configuration import *

branch = "master"
what = sys.argv[1]

if len(sys.argv) >= 3:
    branch = sys.argv[2]

if what is apache_factory:
    steps = [
        run_as_su(
            concatenate(
                cd("/root"),
                mkdir(apache_factory),
                cd(apache_factory),
                git_clone_to_recursive_submodules("https://github.com/milos85vasic/Apache-Factory.git"),
                git_checkout(branch)
            )
        )
    ]

    run(steps)
    exit()

if what is pyramid_factory:
    steps = [
        run_as_su(
            concatenate(
                cd("/root"),
                mkdir(pyramid_factory),
                cd(pyramid_factory),
                git_clone_to_recursive_submodules("https://github.com/milos85vasic/Pyramid-Factory.git"),
                git_checkout(branch)
            )
        )
    ]

    run(steps)
    exit()

print("Not recognized: " + what)
exit(1)
