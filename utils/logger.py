import logging
from datetime import datetime

# set the log file name, ensure there won't be any duplicated name with time stamp
# ":" can't appear in the name, otherwise it will generate error; avoid double "." in the name
file_name = str(datetime.now()).replace(":", "").split(".")[0] + ".log"

# create logger with 'main'
logger = logging.getLogger('main')

# set logger to DEBUG mode
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages, and delay it until the first log message appear, means it will
# not generate an empty log file if the user is not in a test mode
fh = logging.FileHandler(file_name, delay=True)
fh.setLevel(logging.DEBUG)

# set the format of out put
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)

"""
Summary: Using this method instead of the Python "print" method will give you a way to output the log to a local 
        .log file 
Return: void; no return
"""


def log(string: str, test=False):
    if test:
        # In test condition
        # out put the message to logger
        logger.info(string)
        # still display message to console
        print(string)
    else:
        # only print to console
        print(string)
