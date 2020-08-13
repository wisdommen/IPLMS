from abc import abstractmethod, ABCMeta


class UI(metaclass=ABCMeta):
    """ This is the abstract method of the UI class.

    Attributes:
        _layout: a list of layout of the window

    """
    def __init__(self):
        # private element, shouldn't be changed from outside
        _layout = []

    # outside method can get the layout by this method
    def get_layout(self) -> list:
        """ This method returns the list of the layout.

        Returns: a list of the layout.

        """
        return self._layout

    @abstractmethod
    def get_need_validate_fields(self) -> map:
        """ This method returns a map that contains the field should be valid and the rule of validation for each field.

        Returns: a map that contains the field should be valid and the rule of validation for each field.

        """
        pass
