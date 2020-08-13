from src.logic.AbstractLogic import AbstractLogicClass
from abc import ABCMeta, abstractmethod


class AbstractPackingInvoiceClass(AbstractLogicClass, metaclass=ABCMeta):
    """This method inherited the AbstractLogicClass, which is the parent of Packing and Financial class.

    Attributes:
        record: a map if last time chose a record or boolean if last time finished the process
        event: a string id of the event
        values: a map of the values from the window
        data_map: a list of the data (List[Map{str:str}])

    """
    def __init__(self, main, event: str, values: map, record=None):
        super().__init__()
        # The selected record can be a boolean or None, means last time all data is processed or this is
        # a new start, then set the selected record be empty. Otherwise, pass the record that selected
        # last to self.record and ready to be process this time.
        if record is True or record is False or record is None:
            record = {}
        self.data_map = main.pck_inv_data_obj.data_map
        self.event = event
        self.values = values
        self.record = record

    # Overriding method
    def save(self, main, field_map: map) -> None:
        for each in field_map.keys():
            # Creating a record which every field is the header which is values of field map,
            # the values of the record are the values read from the window, get the value by
            # the key field_map which are the key of the input elements in the window
            self.record[field_map[each]] = self.values[each]
        self.update_record(self.record, "Invoice No.")

    @abstractmethod
    def run(self, main):
        pass

