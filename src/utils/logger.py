import logging
import os
from datetime import datetime
from os.path import dirname, exists

# set the log file name, ensure there won't be any duplicated name with time stamp
# ":" can't appear in the name, otherwise it will generate error; avoid double "." in the name
file_name = os.getcwd() + "/log/" + str(datetime.now()).replace(":", "").split(".")[0] + ".log"

# create file if not exists
log_dir = dirname(file_name)
if not exists(log_dir):
    os.makedirs(log_dir)

# create logger with 'main'
logger = logging.getLogger('main')

# set logger to DEBUG mode
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler(file_name, encoding="utf8")
fh.setLevel(logging.DEBUG)

# set the format of out put
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)


def log(string: str) -> None:
    """ Using this method instead of the Python "print" method will give you a way to output the log to a local
    .log file

    Args:
        string: a string that needs to be logged

    Returns: void

    """

    # out put the message to logger
    logger.info(string)
    # still display message to console
    print(string)
