from src.logic.Admin import Admin
from src.logic.Financial import Financial
from src.logic.Login import Login
from src.logic.Packing import Packing
from src.main.MainApplication import MainApplication

import PySimpleGUI as sg

from src.utils import Config
from src.utils.Utils import update_client_list, update_admin_table
from utils.logger import log


class main(MainApplication):

    # Overriding method
    def on_enable(self):
        # documentation see abstract class

        # load config, if no config found, create a new one
        if not Config.is_config_exists():
            Config.save_default_config()
        config = Config.get_config()

        # if use database (not in use, please ignore)
        if config["enable_database"] == "true":
            log("connecting to the database...")
            log("")
            pass

        # set up login page
        login = sg.Window("IPLMS - Login", self.login_ui.get_layout(), auto_size_buttons=False,
                          background_color="lightgray", no_titlebar=True, grab_anywhere=True, size=(300, 300),
                          use_default_focus=True, border_depth=1)
        self.windows_map["login"] = login

        # main loop of the program
        while True:
            event, values = login.read(timeout=300)

            if values["_USERNAME_"] != "":
                login.grab_any_where_off()
            else:
                login.grab_any_where_on()

            log(event + " " + str(values))

            # "X" on the windows top was pressed
            if event == "_LG_CROSS_":
                break
            if event != "_LOGIN_":
                continue
            login_logic = Login(values["_USERNAME_"], values["_PASSWORD_"])
            passport = login_logic.get_login(self.user_data_obj)
            if not passport:
                # show message box
                main.mg.show_warning_box("Your username or password is not correct!")
                continue
            department = login_logic.get_department()
            login.hide()
            record = None

            # start the logic
            # if the identity is financial department
            if department == "financial":
                financial = self.create_window("financial", "IPLMS - Invoice Data Entry Form",
                                               self.financial_ui.get_layout())
                update_client_list(self, financial, "_FA_CLIENT_CB_")
                flag = True
                while flag:
                    event, values = financial.read()
                    log(event + " " + str(values))
                    financial_logic = Financial(self, event, values, record)
                    flag = financial_logic.run(self)
                    record = flag
                break
            # if the identity is loading department
            elif department == "packing":
                packing = self.create_window("packing", "IPLMS - Packing List Data Entry Form",
                                             self.packing_ui.get_layout())
                update_client_list(self, packing, "_PL_CLIENT_CB_")
                flag = True
                while flag:
                    event, values = packing.read()
                    log(event + " " + str(values))
                    packing_logic = Packing(self, event, values, record)
                    flag = packing_logic.run(self)
                    record = flag
                break
            # if the identity is admin
            elif department == "admin":
                admin = self.create_window("admin", "Invoice and Packing List Management System",
                                           self.admin_ui.get_layout())
                update_admin_table(self, self.pck_inv_data_obj.data_map)
                flag = True
                while flag:
                    event, values = admin.read()
                    log(event + " " + str(values))
                    admin_logic = Admin(self, event, values)
                    flag = admin_logic.run(self)
                break

    # Overriding method
    def on_disable(self):
        # documentation see abstract class

        # save the data and close windows
        for each_data in self.data.keys():
            if each_data.save_data() is False:
                log("Permission error")
        for window in self.windows_map.values():
            window.close()


if __name__ == "__main__":
    # init the application main object
    main = main()
    # start of the program
    main.on_enable()
    # end of the program
    main.on_disable()
