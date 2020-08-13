from src.beans.AbstractDataMap import DataMap


class PackingInvoiceData(DataMap):
    """This class load, save and control the packing list and invoice data.

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
        self._file_name = "PackingInvoiceData.csv"
        self.header = ["Invoice No.", "Client Name", "S/C No.", "Date", "Destination port",
                       "Goods description", "Unit price", "Quantity", "Bags", "Net weight", "Gross weight",
                       "Total Measurement"]

    def get_record_by_inv(self, invoice_number: str) -> map:
        """
        The method can get the whole record by its invoice number

        Args:
            invoice_number: a String represents the invoice ID

        Returns: a Map contains all information of a record

        """
        for each in self.data_map:
            if invoice_number == each["Invoice No."]:
                return each

    def is_record_exist(self, record: map) -> bool:
        """
        Check if the record exists

        Args:
            record: a MAP of a record

        Returns: a boolean if the record exists

        """
        for each in self.data_map:
            if each == record:
                return True
        return False
