import csv

from beans.dataMap import DataMap
from utils.csvFileReader import read_csv_file


class UserData(DataMap):

    def __init__(self):
        self.file_name = "UserData.csv"
        self.header = ["department", "username", "password", "is_blocked"]
        self.data_map = []

    def init_data(self):
        self.data_map = read_csv_file(self.file_name, self.header, self.get_file_path(self.file_name))

    def init_file(self):
        DataMap.make_dirs()
        with open(self.get_file_path(self.file_name), "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.header)

    def save_data(self, data_list):
        if len(data_list) > 0:
            records = []
            for data_map in data_list:
                record = []
                for each in self.header:
                    if data_map[each] == "DATA BROKEN":
                        data_map[each] = ''
                    record.append(data_map[each])
                records.append(record)
            try:
                if len(records) == 1:
                    for each in records:
                        for string in each:
                            if string != '':
                                with open(self.get_file_path(self.file_name), "w+") as f:
                                    writer = csv.writer(f)
                                    writer.writerows(records)
                                return
            except PermissionError:
                return False
