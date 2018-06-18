import sys
from commands import *
from configuration import *
from system_configuration import *


def user_home():
    return get_home_directory_path(account)


def get_mysql_bin_directory():
    # MySQL 8.0:
    # return user_home() + "/" + mysql + "/" + mysql_installation_dir + "/usr/local/mysql/bin"
    # MySQL 5.5.60:
    return user_home() + "/" + mysql + "/" + mysql_bin_dir


def get_mysql_logs_directory():
    return user_home() + "/" + mysql + "/" + mysql_log_dir


def get_start_command(account_home):
    return "/mysqld --defaults-extra-file=" + account_home + "/" + mysql + "/" + mysql_conf_dir + "/my.cnf &"


def get_start_command_init(account_home):
    return "/mysqld --defaults-extra-file=" + account_home + "/" + mysql + "/" + mysql_conf_dir \
           + "/my.cnf --init-file=" + account_home + "/" + apache_factory + "/" + mysql_init_tmp + " &"


# MySQL 5.5.60:
def get_mysql_start_command(user_account):
    mysql_full_path = get_home_directory_path(user_account) + "/" + mysql + "/"
    port = default_port_mysql
    if user_account in system_configuration:
        if key_configuration_port_mysql in system_configuration[user_account]:
            port = system_configuration[user_account][key_configuration_port_mysql]

    return mysql_full_path + mysql_bin_dir + "/mysqld --tmpdir=" + mysql_full_path + "tmp --datadir=" \
           + mysql_full_path + "data " + "--secure-file-priv=" + mysql_full_path + "priv --port=" + str(port) \
           + " --user=" + user_account + " " + "--socket=" + mysql_full_path + "socket &"


account = sys.argv[1]
mysql_init_tmp = "init.tmp"

system_configuration = get_system_configuration()

# MySQL 8.0:
initialize = "/mysqld --defaults-file=" + user_home() + "/" + mysql + "/" + mysql_conf_dir + \
             "/my.cnf --initialize --user=" + account

