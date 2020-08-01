import os
from abc import abstractmethod, ABCMeta


class DataMap(metaclass=ABCMeta):

    def is_file_exists(self, file_name):
        path = self.get_file_path(file_name)
        return os.path.exists(path)

    @staticmethod
    def get_file_path(file_name):
        return os.getcwd() + "/database/" + file_name

    @staticmethod
    def make_dirs():
        if not os.path.exists(os.getcwd() + "/database"):
            os.makedirs(os.getcwd() + "/database")

    @abstractmethod
    def init_data(self):
        pass

    @abstractmethod
    def init_file(self):
        pass

    @abstractmethod
    def save_data(self, data_list):
        pass
