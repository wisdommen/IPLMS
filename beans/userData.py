import csv
import os

from beans.dataMap import DataMap
from utils.csvFileReader import read_csv_file


class UserData(DataMap):

    def __init__(self):
        self.file_name = "UserData.csv"
        self.header = ["username", "password"]

    def get_data(self):
        return read_csv_file(self.file_name, self.header, self.get_file_path(self.file_name))

    def init_file(self):
        DataMap.make_dirs()
        with open(self.get_file_path(self.file_name), "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.header)

    def save_data(self):
        pass
