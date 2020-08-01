from main.MainApplication import MainApplication


class NewUser(object):
    def __init__(self, event, values):
        self.data_map = MainApplication.pck_inv_data_obj.data_map
        self.event = event
        self.values = values

    def add_record(self, map):
        self.data_map.append(map)

    def remove_record(self, map):
        self.data_map.remove(map)

    def run(self, main):
        if self.event == "_NU_CREATE_BTN_":
            return True
        elif self.event == "_NU_CANCEL_BTN" or self.event is None:
            return False
        else:
            return True