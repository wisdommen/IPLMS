from src.beans.AbstractDataMap import DataMap


class ClientData(DataMap):
    """This class load, save and control the client data.

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
        self._file_name = "ClientData.csv"
        self.header = ["Client ID", "Client Name", "Client Phone Number", "Client Address"]

