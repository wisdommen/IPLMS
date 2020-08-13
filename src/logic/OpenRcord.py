from PySimpleGUI import Window


class OpenRecord(object):
    """
        This class implements the logic of load a record into the particular window
    """
    def __init__(self, event, values):
        self.event = event
        self.values = values
        self.record = {}

    def run(self, window: Window, fields: list) -> map:
        """ This method control the logic of load records selection window
        
        Args:
            window: the window contains the table
            fields: the fields that need to be get

        Returns: a map that contains selected record data

        """""

        info = window.Element('_OR_TABLE_').get()[self.values["_OR_TABLE_"][0]]
        window.close()
        i = 0
        for each in fields:
            self.record[each] = info[i]
            i += 1
        return self.record


