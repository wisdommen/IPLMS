import os
from threading import Thread

import yaml


def is_config_exists():
    return os.path.exists(os.getcwd() + "\\config\\config.yml")


def get_config():
    if is_config_exists():
        with open(os.getcwd() + "\\config\\config.yml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config


def save_default_config():
    config = {"enable_database": False, "ip": "localhost", "port": 3306, "username": "root", "password": "root", "database":"IPLMS"}
    if not os.path.exists(os.getcwd() + "\\config"):
        os.makedirs(os.getcwd() + "\\config")
    with open(os.getcwd() + "\\config\\config.yml", "w") as f:
        yaml.dump(config, f)


def reload_config():
    pass
