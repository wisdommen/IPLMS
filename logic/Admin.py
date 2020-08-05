from logic.AbstractPackingInvoice import AbstractPackingInvoiceClass
from logic.UserManage import UserManage


class Admin(AbstractPackingInvoiceClass):

    def run(self, main):
        if self.event == "_AD_OPEN_BTN_":
            # TODO complete open the record by excel(generate the excel file)
            return True
        elif self.event == "_AD_EDIT_BTN_":
            # TODO complete opening a window that can modify the record
            return True
        elif self.event == "_AD_DEL_BTN_":
            # TODO delete a selected record
            # TODO show message box
            return True
        elif self.event == "_AD_SEARCH_BTN":
            # TODO the search
            return True
        elif self.event == "_AD_UGM_BTN_":
            # user_manage = main.create_window("user_manage", "IPLMS",
            #                                  main.user_manage_ui.get_layout(),
            #                                  disable_close=True)
            # user_manage.un_hide()
            # event, values = user_manage.read()
            # user_manage_logic = UserManage(main, event, values)
            # user_manage_logic.run(main)
            # user_manage.hide()
            return True
        elif self.event == "_AD_QUIT_BTN_" or self.event is None:
            # TODO show message box
            # TODO ask for saving the unsaved changes
            return False
        else:
            return True


