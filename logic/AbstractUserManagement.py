from logic.AbstractLogic import AbstractLogicClass
from abc import ABCMeta, abstractmethod


class AbstractUserManagementClass(AbstractLogicClass, metaclass=ABCMeta):
    def __init__(self, main, event, values):
        super().__init__()
        self.data_map = main.user_data_obj.data_map
        self.event = event
        self.values = values

    def save(self, main, field_map: map) -> None:
        for each in field_map.keys():
            self.record[field_map[each]] = self.values[each]
        self.update_record(self.record, "department")

    @abstractmethod
    def run(self, main):
        pass
