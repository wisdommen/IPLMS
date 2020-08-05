import csv

from beans.AbstractDataMap import DataMap
from utils.csvFileReader import read_csv_file


class ClientData(DataMap):
    """This class load, save and control the client data.

    You can load the data and save the data through this class after instantiate the class.

    Attributes:
        _file_name: a string of the data file name. (Private variable)
        header: a list of the data file header (csv file header). (Private variable)
        data_map: a list of all data maps of client data
    """

    def __init__(self):
        """
        Initiate the class with these data
        """
        self._file_name = "ClientData.csv"
        self.header = ["Client ID", "Client Name", "Client Phone Number", "Client Address"]
        self.data_map = []

    # Overriding method
    def init_data(self):
        self.data_map = read_csv_file(self._file_name, self.header, self.get_file_path(self._file_name))

    # Overriding method
    def init_file(self):
        try:
            DataMap.make_dirs()
            with open(self.get_file_path(self._file_name), "w") as f:
                writer = csv.writer(f)
                writer.writerow(self.header)
        except PermissionError:
            return False

    # Overriding method
    def save_data(self, data_list):
        if len(data_list) > 0:
            records = []
            for data_map in data_list:
                record = []
                for each in self.header:
                    record.append(data_map.get(each, defult=""))
                records.append(record)
            try:
                if len(records) > 1:
                    for each in records:
                        for string in each:
                            if string != '':
                                with open(self.get_file_path(self._file_name), "w", encoding='utf8', newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow(self.header)
                                    for record in records:
                                        writer.writerow(record)
                                return
            except PermissionError:
                return False
