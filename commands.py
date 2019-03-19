import os

here = "./"


def run_as_su(what):
    return 'su -c "' + what + '"'


def sudo(what):
    return "sudo " + what


def get_yum(*what):
    items = ""
    for item in what:
        items += item + " "
    return "yum install -y " + items


def get_yum_group(what):
    return "yum groups install -y '" + what + "'"


def concatenate(*what):
    result = ""
    for item in what:
        append = item.strip()
        if append:
            result += " " + append
            if what.index(item) < len(what) - 1:
                result += ";"
    return result


def clear():
    return "clear"


def wget(what, **params):
    destination = 'destination'
    if destination in params:
        return wget(what) + " -P " + params[destination]
    else:
        return "wget " + what


def curl(url):
    return "curl " + url


def mkdir(dir_name):
    return "mkdir " + dir_name


def mkdirs(directories):
    param = ""
    for directory in directories:
        param += " " + directory
    return "mkdir " + param


def extract(what, **params):
    destination = 'destination'
    if destination in params:
        return "tar  -xvzf " + what + " --directory " + params[destination]
    else:
        return "tar  -xvzf " + what


def cd(where):
    return "cd " + where


def mv(what, where):
    return "mv " + what + " " + where


def cp_dir(what, where):
    return "cp -a " + what + "/. " + where + "/"


def cp(what, where):
    return "cp " + what + " " + where


def run(what):
    for cmd in what:
        os.system(cmd)


def add_user(user):
    return "adduser " + user


def add_group(group):
    return "groupadd " + group


def passwd(user):
    return "passwd " + user


def run_as_user(account, command):
    return "sudo -H -u " + account + " bash -c '" + command + "'"


def git_clone(what):
    return "git clone " + what


def git_clone_recursive(what):
    return "git clone " + what + " --recursive"


def git_submodule_init():
    return "git submodule init"


def git_submodule_checkout_each():
    return "git submodule foreach --recursive git checkout master"


def git_submodule_update():
    return "git submodule update"


def git_clone_to(what, where):
    return "git clone " + what + " " + where


def git_clone_to_recursive(what, where):
    return "git clone " + what + " " + where + " --recursive"


def git_clone_to_recursive_submodules(what):
    return "git clone --recurse-submodules " + what + " ./"


def git_checkout(what):
    return "git checkout " + what


def python(script, *params):
    if os.path.isfile(script):
        arguments = ""
        for item in params:
            arguments += " " + item
        if not arguments:
            return "python " + script
        else:
            return "python " + script + " " + arguments
    return "echo 'No script named " + script + "'"


def rm(what):
    return "rm -rf " + what


def rm_files(what):
    return "rm " + what


def apache_start():
    return "./apachectl start"


def pyramid_setup(variant):
    return "python setup.py " + variant


def pyramid_start():
    return "pserve pyramid_factory.ini &"


def apache_stop():
    return "./apachectl stop"


def chmod(where, mode):
    return "chmod -R " + mode + " " + where


def chmodx(what):
    return "chmod +x " + what


def chgrp(group, directory):
    return "chgrp -R " + group + " " + directory


def chown(account, directory):
    return "chown -R " + account + " " + directory


def pwd():
    return "pwd"


def ls():
    return "ls -lF"


def sleep(seconds):
    return "sleep " + str(seconds)


def add_to_group(account, group):
    return "usermod -a -G " + group + " " + account


def output(what, where):
    return 'echo "' + what + '" > ' + where


def pip_upgrade():
    return "pip install --upgrade pip"


def pip(what):
    return "pip install " + what


def kill(who):
    return "kill " + who


def echo(what):
    return "echo \"" + what + "\""


def venv_init():
    return "virtualenv env"


def venv_activate():
    return "source env/bin/activate"


def venv_deactivate():
    return "deactivate"
