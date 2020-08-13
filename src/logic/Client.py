from src.logic.AbstractLogic import AbstractLogicClass
from src.main.MainApplication import MainApplication
from src.utils.Utils import load_record, validate_input


class Client(AbstractLogicClass):
    def __init__(self, main, event, values):
        super().__init__()
        self.data_map = main.client_data_obj.data_map
        self.event = event
        self.values = values
        self.record = {}

    # Overriding method
    def run(self, main: MainApplication) -> str:
        # documentation see abstract class

        # The field_data formed by the window elements' key as key and the corresponding header of the data_map as
        # values
        field_data = {
            "_CLIENT_ID_": "Client ID",
            "_CP_NAME_IP_": "Client Name",
            "_CP_PHONE_IP_": "Client Phone Number",
            "_CP_ADDRESS_IP_": "Client Address"
        }
        # method of save record
        if self.event == "_CP_SAVE_BTN_":
            # check validation
            result = validate_input(main.client_ui, field_data, self.values)
            if len(result) > 0:
                string_builder = ""
                for each in result:
                    string_builder = string_builder+each+"\n"
                main.mg.show_warning_box(string_builder)
                # start again, looping
                event, values = main.windows_map["client"].read()
                self.event = event
                self.values = values
                self.run(main)
            self.save(main, field_data)
            # show message box
            main.mg.show_info_box("Record Saved!")
            return self.values.get("_CP_NAME_IP_", "")
        # method of cancel button pressed (actually do nothing)
        elif self.event == "_CP_CANCEL_BTN":
            return ""
        elif self.event == "Open":
            # load the record from existing database
            self.record = load_record(self, main, main.client_data_obj, "client", field_data)
            # start again, looping
            event, values = main.windows_map["client"].read()
            self.event = event
            self.values = values
            self.run(main)

    # Overriding method
    def save(self, main: MainApplication, field_data: map) -> None:
        # documentation see abstract class
        window = main.windows_map["client"]
        for each in field_data.keys():
            if each == "_CLIENT_ID_":
                self.record["Client ID"] = window["_CLIENT_ID_"].DisplayText
                continue
            self.record[field_data[each]] = self.values[each]
        self.update_record(self.record, "Client ID")
