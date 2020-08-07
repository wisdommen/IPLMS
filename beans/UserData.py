import csv

from beans.AbstractDataMap import DataMap
from utils.csvFileReader import read_csv_file


class UserData(DataMap):

    def __init__(self):
        self._file_name = "UserData.csv"
        self.header = ["department", "username", "password", "is_blocked"]
        self.data_map = []

    # Override
    def init_data(self):
        self.data_map = read_csv_file(self._file_name, self.header, self.get_file_path(self._file_name))

    # Override
    def init_file(self):
        DataMap.make_dirs()
        with open(self.get_file_path(self._file_name), "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.header)

    # Override
    def save_data(self):
        if len(self.data_map) > 0:
            records = []
            for data_map in self.data_map:
                record = []
                for each in self.header:
                    record.append(data_map.get(each, ""))
                records.append(record)
            try:
                if len(records) > 1:
                    with open(self.get_file_path(self._file_name), "w", encoding='utf8', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(self.header)
                        for record in records:
                            writer.writerow(record)
            except PermissionError:
                return False
