from logic.AbstractLogic import AbstractLogicClass
from abc import ABCMeta, abstractmethod


class AbstractPackingInvoiceClass(AbstractLogicClass, metaclass=ABCMeta):
    def __init__(self, main, event, values, record=None):
        super().__init__()
        if record is True or record is False or record is None:
            record = {}
        self.data_map = main.pck_inv_data_obj.data_map
        self.event = event
        self.values = values
        self.record = record

    def save(self, main, field_map: map) -> None:
        for each in field_map.keys():
            self.record[field_map[each]] = self.values[each]
        self.update_record(self.record, "Invoice No.")

    @abstractmethod
    def run(self, main):
        pass

