import os
from abc import abstractmethod, ABCMeta


class DataMap(metaclass=ABCMeta):
    """This is the abstract class for all data operation class.

    All data method should inherit this class and instantiate all abstract
    methods.

    """
    def __init__(self):
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

    @abstractmethod
    def init_data(self) -> None:
        """
        Load all data file into memory here.
        Load all data with data validation

        :return: void
        """
        pass

    @abstractmethod
    def init_file(self) -> None or bool:
        """
        Check if the data file is exists or not, if the file is missing
        create the default empty data and data folder

        :return: void
        """
        pass

    @abstractmethod
    def save_data(self) -> None or bool:
        """
        Save the data from the memory to the disk.
        Save the file with data validation.

        :return: void
        """
        pass


# TODO use the client id in the pck_data instead of client name