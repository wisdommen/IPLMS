from logic.NewUser import NewUser
from main.MainApplication import MainApplication


class UserManage(object):
    def __init__(self, event, values):
        self.data_map = MainApplication.pck_inv_data_obj.data_map
        self.event = event
        self.values = values

    def add_record(self, map):
        self.data_map.append(map)

    def remove_record(self, map):
        self.data_map.remove(map)

    def run(self, main):
        if self.event == "_UM_CREATE_BTN_":
            new_user = main.create_window("new_user", "IPLMS",
                                          MainApplication.new_user_ui.get_layout(),
                                          disable_close=True)
            new_user.un_hide()
            new_user.bring_to_front()
            event7, values7 = new_user.read()
            print(event7, values7)
            new_user_logic = NewUser(event7, values7)
            new_user_logic.run(main)
            new_user.hide()
            event, values = main.windows_map["user_manage"].read()
            self.event = event
            self.values = values
            self.run(main)
            return True
        elif self.event == "_UM_SAVE_BTN_":
            return True
        elif self.event == "_UM_QUIT_BTN_" or self.event is None:
            return False
        else:
            return True