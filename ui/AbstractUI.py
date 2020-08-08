from abc import abstractmethod, ABCMeta


class UI(metaclass=ABCMeta):
    # private element, shouldn't be changed from outside
    _layout = []

    # outside method can get the layout by this method
    def get_layout(self):
        return self._layout

    @abstractmethod
    def get_need_validate_fields(self):
        pass
