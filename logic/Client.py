from logic.OpenRcord import OpenRecord
from main.MainApplication import MainApplication


class Client(object):
    def __init__(self, event, values):
        self.data_map = MainApplication.client_data_obj.data_map
        self.event = event
        self.values = values
        self.record = {}

    def add_record(self, record_map):
        for each in self.data_map:
            if each["Client ID"] == record_map["Client ID"]:
                self.data_map.remove(each)
        self.data_map.append(record_map)

    def remove_record(self, record_map):
        self.data_map.remove(record_map)

    def run(self, main):
        if self.event == "_CP_SAVE_BTN_":
            self.record["Client ID"] = main.windows_map["client"]["_CLIENT_ID_"].DisplayText
            self.record["Client Name"] = self.values["_CP_NAME_IP_"]
            self.record["Client Phone Number"] = self.values["_CP_PHONE_IP_"]
            self.record["Client Address"] = self.values["_CP_ADDRESS_IP_"]
            self.add_record(self.record)
        elif self.event == "_CP_CANCEL_BTN":
            pass
        elif self.event == "Open":
            header = ["Client ID", "Client Number", "Client Phone Number", "Client Address"]
            opened_records = main.create_open_record_window(len(self.data_map), len(header), self.data_map, header)
            opened_records.un_hide()
            event, values = opened_records.read()
            print(event, values)
            open_record_logic = OpenRecord(event, values)
            try:
                self.record = open_record_logic.run(opened_records)
            except IndexError:
                values = {'_OR_TABLE_': [0]}
                open_record_logic = OpenRecord(event, values)
                self.record = open_record_logic.run(opened_records)
            if event != "_OR_CAN_BTN_":
                if event == "_OR_DEL_BTN_":
                    self.remove_record(self.record)
                main.windows_map["client"]["_CLIENT_ID_"].Update(self.record["Client ID"])
                main.windows_map["client"]["_CP_NAME_IP_"].Update(self.record["Client Name"])
                main.windows_map["client"]["_CP_PHONE_IP_"].Update(self.record["Client Phone Number"])
                main.windows_map["client"]["_CP_ADDRESS_IP_"].Update(self.record["Client Address"])

            event, values = main.windows_map["client"].read()
            self.event = event
            self.values = values
            self.run(main)
