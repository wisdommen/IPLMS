from src.logic.AbstractUserManagement import AbstractUserManagementClass
from src.main.MainApplication import MainApplication


class NewUser(AbstractUserManagementClass):
    """
    This class is not going to be completed due to the time constrain, but the reason I keep it here
    is I want to complete this in the future, please ignore everything in this class
    """

    # Overriding method
    def run(self, main: MainApplication) -> bool:
        # documentation see abstract class

        if self.event == "_NU_CREATE_BTN_":
            # save the entered information as user group
            return True
        elif self.event == "_NU_CANCEL_BTN" or self.event is None:
            # ask for saving the unsaved changes
            return False
        else:
            return True
