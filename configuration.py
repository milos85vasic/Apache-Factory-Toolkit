apache_factory = "Apache-Factory"

php = "Php"
mysql = "MySQL"
apache2 = "Apache2"
mysql_bin_dir = "Bin"
mysql_lib_dir = "Lib"
mysql_data_dir = "Data"
mysql_log_dir = "Log"
mysql_tmp_dir = "Tmp"
mysql_sock_dir = "Sock"
mysql_pid_dir = "Pid"
mysql_share_dir = "Share"
mysql_conf_dir = "Conf"
mysql_installation_dir = "Release"

default_port = 8080
default_port_mysql = 3306
account_json = "account.json"
apache_factory_group = "apache_factory"
apache_factory_configuration_dir = "/usr/share/apache_factory"
default_configuration_json = apache_factory_configuration_dir + "/global_configuration.json"

wipe_script = "wipe.py"
content_dir_name = "Content"


def get_home_directory_path(account):
    return "/home/" + account


def content_dir_path(home_path):
    return home_path + "/" + content_dir_name
