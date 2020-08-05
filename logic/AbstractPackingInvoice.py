from logic.AbstractLogic import AbstractLogicClass
from abc import ABCMeta, abstractmethod


class AbstractPackingInvoiceClass(AbstractLogicClass, metaclass=ABCMeta):
    def __init__(self, main, event, values):
        super().__init__()
        self.data_map = main.pck_inv_data_obj.data_map
        self.event = event
        self.values = values

    def add_record(self, record_map, record_id):
        for each in self.data_map:
            if each[record_id] == record_map[record_id]:
                self.data_map.remove(each)
        self.data_map.append(record_map)

    def save(self, main, field_map):
        for each in field_map.keys():
            self.record[field_map[each]] = self.values[each]
        self.add_record(self.record, "Invoice No.")

    @abstractmethod
    def run(self, main):
        pass

