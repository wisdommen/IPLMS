import csv

from beans.AbstractDataMap import DataMap
from utils.csvFileReader import read_csv_file


def init(path, header):
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)


class PackingInvoiceData(DataMap):

    def __init__(self):
        super().__init__()
        self._file_name = "PackingInvoiceData.csv"
        self.header = ["Invoice No.", "Client Name", "S/C No.", "Date", "Destination port",
                       "Goods description", "Unit price", "Quantity", "Bags", "Net weight", "Gross weight",
                       "Total Measurement"]

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

    def get_record_by_inv(self, invoice_number):
        for each in self.data_map:
            if invoice_number == each["Invoice No."]:
                return each

    def is_record_exist(self, record):
        for each in self.data_map:
            if each == record:
                return True
        return False
