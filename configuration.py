apache_factory = "Apache-Factory"
pyramid_factory = "Pyramid-Factory"

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
factory_script = "factory.py"
distribution_script = "distribute.py"
find_service_index_script = "find_service_index.py"
services_distribution_script = "distribute_services.py"

content_dir_name = "Content"
service_indexes = ["index.html", "index.htm", "index.php", "setup.py"]

rpm_fusion_free = "https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm"
rpm_fusion_non_free = "https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm"


def get_home_directory_path(account):
    return "/home/" + account


def content_dir_path(home_path):
    return home_path + "/" + content_dir_name
