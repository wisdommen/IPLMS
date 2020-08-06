from abc import abstractmethod, ABCMeta


class AbstractLogicClass(metaclass=ABCMeta):
    def __init__(self):
        self.data_map = None
        self.record = {}

    def update_record(self, record_map, record_id):
        for each in self.data_map:
            # UPDATE DATA IF EXISTS
            if each[record_id] == record_map[record_id]:
                for field in record_map.keys():
                    each[field] = record_map[field]
                return
        self.data_map.append(record_map)

    def remove_record(self, record_map):
        self.data_map.remove(record_map)

    @abstractmethod
    def run(self, main):
        pass

    @abstractmethod
    def save(self, main, field_map):
        pass
