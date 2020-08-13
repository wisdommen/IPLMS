from src.beans.AbstractDataMap import DataMap


class UserData(DataMap):
    """This class load, save and control the user data.

    You can load the data and save the data through this class after instantiate the class.

    Attributes:
        _file_name: a string of the data file name. (Private variable)
        header: a list of the data file header (csv file header). (Private variable)
    """

    def __init__(self):
        """
        Initiate the class with these data
        """
        super().__init__()
        self._file_name = "UserData.csv"
        self.header = ["department", "username", "password", "is_blocked"]

