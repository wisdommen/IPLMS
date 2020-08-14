import os

# import yaml module
from utils.logger import log

try:
    import yaml
except ModuleNotFoundError:
    log("WARNING! No module found, start installing the required module...")
    try:
        os.system("pip3 install PyYaml")
        import yaml
    except:
        log("ERROR! Can't import required PyYaml module, stopping...")
        exit(1)

"""
    This class is not going to be completed due to the time constrain, but the reason I keep it here
    is I want to complete this in the future, please ignore everything in this class
"""


def is_config_exists() -> bool:
    return os.path.exists(os.getcwd() + "/config/config.yml")


def get_config() -> map:
    if is_config_exists():
        with open(os.getcwd() + "/config/config.yml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config


def save_default_config() -> None:
    config = {"enable_database": False, "ip": "localhost", "port": 3306, "username": "root", "password": "root",
              "database": "IPLMS"}
    if not os.path.exists(os.getcwd() + "/config"):
        os.makedirs(os.getcwd() + "/config")
    with open(os.getcwd() + "/config/config.yml", "w") as f:
        yaml.dump(config, f)


def reload_config():
    pass
