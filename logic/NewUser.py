from logic.AbstractUserManagement import AbstractUserManagementClass


class NewUser(AbstractUserManagementClass):

    def run(self, main):
        if self.event == "_NU_CREATE_BTN_":
            # TODO save the entered information as user group
            return True
        elif self.event == "_NU_CANCEL_BTN" or self.event is None:
            # TODO ask for saving the unsaved changes
            return False
        else:
            return True
