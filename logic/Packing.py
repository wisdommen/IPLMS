from logic.Client import Client
from main.MainApplication import MainApplication
from utils.Utils import getUUID


class Packing(object):
    def __init__(self, event, values):
        self.data_map = MainApplication.pck_inv_data_obj.data_map
        self.event = event
        self.values = values

    def add_record(self, map):
        self.data_map.append(map)

    def remove_record(self, map):
        self.data_map.remove(map)

    def run(self, main):
        if self.event == "_PL_NEW_BTN_":
            client = main.create_window("client", "IPLMS", MainApplication.client_ui.get_layout(), disable_close=True)
            client["_CLIENT_ID_"].Update(getUUID())
            client["_CP_NAME_IP_"].Update("")
            client["_CP_PHONE_IP_"].Update("")
            client["_CP_ADDRESS_IP_"].Update("")
            client.un_hide()
            event4, values4 = client.read()
            print(event4, values4)
            client_logic = Client(event4, values4)
            client_logic.run(main)
            client.hide()
            return True
        elif self.event == "_PL_LOAD_BTN_":
            return True
        elif self.event == "_PL_CLA_BTN_":
            return True
        elif self.event == "_PL_SAVE_BTN_":
            return True
        elif self.event == "_PL_QUIT_BTN_" or self.event is None:
            return False
        else:
            return True