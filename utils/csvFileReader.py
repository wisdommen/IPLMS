import csv
import os

from utils.logger import log

"""
Summary: this method is used to read the data from the local csv file.
Return: None if error occurs; otherwise return a (list)data_list read from the local file
"""


def read_csv_file(file_name: str, header: list, file_path="", test=False) -> list or None:
    # initiate a private data list
    data_temp = []
    try:
        # Get the data from the local .csv file if the data list is empty
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            # Check if the csv file contains data
            try:
                # Check if the header is in the csv file missing or broken
                if header not in reader:
                    log("Warning! The header in '%s' is BROKEN or MISSING!" % file_name, test)
                    return None
                for i in reader:
                    # get rid of the headers
                    if i != header:
                        # check if there is any exact same record in the data list
                        data_map = {}
                        for k in range(len(header)):
                            try:
                                if i[k] == '':
                                    i[k] = "DATA BROKEN"
                                data_map[header[k]] = i[k]
                            except IndexError:
                                data_map[header[k]] = "DATA BROKEN"
                        if data_map in data_temp:
                            log("Warning! Absolute duplicate recode detected!", test)
                            log("Duplicated Record: %s" % str(i), test)
                            log("Until now there is %d duplicated record found!" % (data_temp.count(i) + 1), test)
                        data_temp.append(data_map)
                if len(data_temp) == 0:
                    log("Warning! There is no record in the '%s' file!" % file_name, test)
                    return None
                return data_temp
            # if the csv file is empty, trow warning and return False
            except IndexError as e:
                log(str(e), test)
                log("Error occurs while reading '%s' file!" % file_name, test)
                log("File damaged! Please check the '%s' file's content!" % file_name, test)
                return None
    # if the csv file is missing, trow warning and return False
    except FileNotFoundError as e:
        # an empty csv file still can trow a FileNotFoundError, so we should judge if it is missing or just empty
        csv_file_names = []
        files = os.listdir(file_path[:-1])
        for i in files:
            if os.path.splitext(i)[1] == ".csv":
                csv_file_names.append(i)
        if file_name in files:
            log("Error occurs while loading '%s' file!" % file_name, test)
            log("'%s' file is empty!" % file_name, test)
            return None
        log(str(e), test)
        log("Error occurs while loading '%s' file!" % file_name, test)
        log("File not found! Please check if the '%s' exists in the folder!" % file_name, test)
        return None
    # if the program does not have permission to open the file, trow warning and return False
    except PermissionError as e:
        log(str(e), test)
        log("Error occurs while loading '%s' file!" % file_name, test)
        log("The program does not have permission to open '%s'!" % file_name, test)
        return None
