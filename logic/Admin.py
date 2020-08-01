from logic.UserManage import UserManage
from main.MainApplication import MainApplication


class Admin(object):
    def __init__(self, event, values):
        self.data_map = MainApplication.pck_inv_data_obj.data_map
        self.event = event
        self.values = values

    def add_record(self, map):
        self.data_map.append(map)

    def remove_record(self, map):
        self.data_map.remove(map)

    def run(self, main):
        if self.event == "_AD_OPEN_BTN_":
            return True
        elif self.event == "_AD_EDIT_BTN_":
            return True
        elif self.event == "_AD_DEL_BTN_":
            return True
        elif self.event == "_AD_UGM_BTN_":
            user_manage = main.create_window("user_manage", "IPLMS",
                                             MainApplication.user_manage_ui.get_layout(),
                                             disable_close=True)
            user_manage.un_hide()
            event, values = user_manage.read()
            user_manage_logic = UserManage(event, values)
            user_manage_logic.run(main)
            user_manage.hide()
            return True
        elif self.event == "_AD_QUIT_BTN_" or self.event is None:
            return False
        else:
            return True


