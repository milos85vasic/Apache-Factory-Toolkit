apache_factory = "Apache-Factory"

php = "Php"
mysql = "MySQL"
apache2 = "Apache2"
mysql_bin_dir = "bin"
mysql_lib_dir = "lib"
mysql_priv_dir = "priv"
mysql_bench_dir = "bench"
mysql_plugin_dir = "plugin"
mysql_data_dir = "data"
mysql_log_dir = "log"
mysql_tmp_dir = "tmp"
mysql_sock_dir = "sock"
mysql_script_dir = "scripts"
mysql_pid_dir = "pid"
mysql_share_dir = "share"
mysql_conf_dir = "conf"
mysql_installation_dir = "release"

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
