from src.logic.AbstractUserManagement import AbstractUserManagementClass
from src.logic.NewUser import NewUser
from src.main.MainApplication import MainApplication


class UserManage(AbstractUserManagementClass):
    """
        This class is not going to be completed due to the time constrain, but the reason I keep it here
        is I want to complete this in the future, please ignore everything in this class
    """

    # Overriding method
    def run(self, main: MainApplication) -> bool:
        # documentation see abstract class

        if self.event == "_UM_CREATE_BTN_":
            new_user = main.create_window("new_user", "IPLMS",
                                          main.new_user_ui.get_layout(),
                                          disable_close=True)
            new_user.un_hide()
            new_user.bring_to_front()
            event7, values7 = new_user.read()
            print(event7, values7)
            new_user_logic = NewUser(main, event7, values7)
            new_user_logic.run(main)
            new_user.hide()
            event, values = main.windows_map["user_manage"].read()
            self.event = event
            self.values = values
            self.run(main)
            return True
        elif self.event == "_UM_SAVE_BTN_":
            # save the user to data_map
            # self.save(main, field_data)
            return True
        elif self.event == "_UM_QUIT_BTN_" or self.event is None:
            # ask for saving the unsaved changes
            return False
        else:
            return True
