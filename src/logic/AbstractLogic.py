from abc import abstractmethod, ABCMeta


class AbstractLogicClass(metaclass=ABCMeta):
    """This abstract class is the parent of every logic class.

    All logic class should inherit this class and instantiate all abstract
    methods.
    """
    def __init__(self):
        self.data_map = None
        self.record = {}

    def update_record(self, record_map: map, record_id: str) -> None:
        """This method will update the record in the memory if it exists or add the record if not exists

        Args:
            record_map: a map which is the record that need to be updated or added
            record_id: the unique record id

        Returns: void

        """
        for each in self.data_map:
            # UPDATE DATA IF EXISTS
            if each[record_id] == record_map[record_id]:
                for field in record_map.keys():
                    each[field] = record_map[field]
                return
        self.data_map.append(record_map)

    def remove_record(self, record_map: map) -> None:
        """This method will remove a record in the data map if exists

        Args:
            record_map: a map which is the record that need to be removed

        Returns: void

        """
        self.data_map.remove(record_map)

    @abstractmethod
    def run(self, main) -> bool:
        """This method contains different way that each child will behave when operating the window elements

        Args:
            main: the main class of the whole program

        Returns: a boolean if the program should run another loop

        """
        pass

    @abstractmethod
    def save(self, main, field_map: map) -> None:
        """This method save the record into the data_map

        Args:
            main: the main class of the whole program
            field_map: a map that contains matches of the window element key and the data map key

        Returns: void

        """
        pass
