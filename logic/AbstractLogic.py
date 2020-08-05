from abc import abstractmethod, ABCMeta


class AbstractLogicClass(metaclass=ABCMeta):
    def __init__(self):
        self.data_map = None
        self.record = {}

    def add_record(self, record_map, record_id):
        for each in self.data_map:
            if each[record_id] == record_map[record_id]:
                self.data_map.remove(each)
        self.data_map.append(record_map)

    def remove_record(self, record_map):
        self.data_map.remove(record_map)

    @abstractmethod
    def run(self, main):
        pass

    @abstractmethod
    def save(self, main, field_map):
        pass
