from logic.AbstractLogic import AbstractLogicClass
from utils.Utils import load_record


class Client(AbstractLogicClass):
    def __init__(self, main, event, values):
        super().__init__()
        self.data_map = main.client_data_obj.data_map
        self.event = event
        self.values = values

    def run(self, main):
        field_data = {
            "_CLIENT_ID_": "Client ID",
            "_CP_NAME_IP_": "Client Name",
            "_CP_PHONE_IP_": "Client Phone Number",
            "_CP_ADDRESS_IP_": "Client Address"
        }

        if self.event == "_CP_SAVE_BTN_":
            self.save(main, field_data)
            # TODO show message box
        elif self.event == "_CP_CANCEL_BTN":
            pass
        elif self.event == "Open":

            load_record(self, main, main.client_data_obj, "client", field_data)

            event, values = main.windows_map["client"].read()
            self.event = event
            self.values = values
            self.run(main)

    def save(self, main, field_data):
        window = main.windows_map["client"]
        for each in field_data.keys():
            if each == "_CLIENT_ID_":
                self.record["Client ID"] = window["_CLIENT_ID_"].DisplayText
                continue
            self.record[field_data[each]] = self.values[each]
        self.add_record(self.record, "Client ID")
