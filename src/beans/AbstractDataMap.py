import csv
import os

from src.utils.csvFileReader import read_csv_file


class DataMap(object):
    """This is the parent class for all data operation class.

    All data class should inherit this class and instantiate all abstract
    methods.

    Attributes:
        _file_name: a string of the data file name. (Private variable)
        header: a list of the data file header (csv file header). (Private variable)
        data_map: a list of the data (List[Map{str:str}])

    """
    def __init__(self):
        self._file_name = ""
        self.data_map = []
        self.header = []

    def is_file_exists(self, file_name: str) -> bool:
        """
        This method check the file is exists or not by the file name.

        :param file_name: A string of the file name
        :return: a boolean if the file exists
        """
        path = self.get_file_path(file_name)
        return os.path.exists(path)

    @staticmethod
    def get_file_path(file_name: str) -> str:
        return os.getcwd() + "/database/" + file_name

    @staticmethod
    def make_dirs() -> None:
        """
        Make the data folder if the folder is not exists

        :return: a boolean of if the folder created successfully or not
        """
        if not os.path.exists(os.getcwd() + "/database"):
            os.makedirs(os.getcwd() + "/database")

    def init_data(self) -> None:
        """
        Load all data file into memory here.
        Load all data with data validation

        :return: void
        """
        self.data_map = read_csv_file(self._file_name, self.header, self.get_file_path(self._file_name))

    def init_file(self) -> None or bool:
        """
        Check if the data file is exists or not, if the file is missing
        create the default empty data and data folder

        :return: void
        """
        # Make the data folder if the folder is not exists
        self.make_dirs()
        # save the default csv file into the data folder which only include header
        with open(self.get_file_path(self._file_name), "w") as f:
            writer = csv.writer(f)
            writer.writerow(self.header)

    def save_data(self) -> None or bool:
        """
        Save the data from the memory to the disk.
        Save the file with data validation.

        :return: void
        """
        # save the data when the data map has more than 1 record
        if len(self.data_map) > 0:
            records = []
            # convert the data map (List[Map{}]) into records (List[List[]])
            for data_map in self.data_map:
                record = []
                for each in self.header:
                    record.append(data_map.get(each, ""))
                records.append(record)
            try:
                # double check if the records has more than 1 record which should not only contain header
                if len(records) > 1:
                    # write the records into the csv file
                    with open(self.get_file_path(self._file_name), "w", encoding='utf8', newline='') as f:
                        writer = csv.writer(f)
                        # should write header first
                        writer.writerow(self.header)
                        for record in records:
                            writer.writerow(record)
            # If the get permissionError means the file can't be wrote
            except PermissionError:
                return False


# TODO use the client id in the pck_data instead of client name