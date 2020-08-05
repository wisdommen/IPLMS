from logic.Admin import Admin
from logic.Financial import Financial
from logic.Login import Login
from logic.Packing import Packing
from main.MainApplication import MainApplication

import PySimpleGUI as sg

from utils import Config


class main(MainApplication):

    # Override
    def on_enable(self):

        # load config, if no config found, create a new one
        if not Config.is_config_exists():
            Config.save_default_config()
        config = Config.get_config()

        # if use database (developing)
        if config["enable_database"] == "true":
            print("connecting to the database...")
            print("")
            pass

        # set up login page
        login = sg.Window("IPLMS - Login", self.login_ui.get_layout(), auto_size_buttons=False,
                          background_color="lightgray", no_titlebar=True, grab_anywhere=True, size=(300, 300),
                          use_default_focus=True, border_depth=1)
        self.windows_map["login"] = login

        while True:
            event, values = login.read(timeout=300)

            if values["_USERNAME_"] != "":
                login.grab_any_where_off()
            else:
                login.grab_any_where_on()

            print(event, values)

            if event != "_LG_CROSS_":
                if event == "_LOGIN_":
                    login_logic = Login(values["_USERNAME_"], values["_PASSWORD_"])
                    passport = login_logic.get_login(self.user_data_obj)
                    if passport == True:
                        department = login_logic.get_department()
                        login.hide()
                        if department == "financial":
                            financial = self.create_window("financial", "IPLMS - Invoice Generator",
                                                           self.financial_ui.get_layout())
                            flag = True
                            while flag:
                                event3, values3 = financial.read()
                                print(event3, values3)
                                financial_logic = Financial(self, event3, values3)
                                flag = financial_logic.run(self)
                            break
                        elif department == "packing":
                            packing = self.create_window("packing", "IPLMS - Packing List Generator",
                                                         self.packing_ui.get_layout())
                            flag = True
                            while flag:
                                event3, values3 = packing.read()
                                print(event3, values3)
                                packing_logic = Packing(self, event3, values3)
                                flag = packing_logic.run(self)
                            break
                        elif department == "admin":
                            header_list = ["Invoice No.", "Client Name", "Data", "Goods description"]
                            self.admin_ui.set_table(header_list, self.pck_inv_data_obj.data_map)
                            admin = self.create_window("admin", "Invoice and Packing List Management System",
                                                       self.admin_ui.get_layout())
                            flag = True
                            while flag:
                                event3, values3 = admin.read()
                                print(event3, values3)
                                admin_logic = Admin(self, event3, values3)
                                flag = admin_logic.run(self)
                            break
                    else:
                        print(passport)
            # "X" on the windows top was pressed
            elif event == "_LG_CROSS_":
                break

    # Override
    def on_disable(self):
        for each_data in self.data.keys():
            if each_data.save_data(self.data[each_data]) is False:
                print("Permission error")
        for window in self.windows_map.values():
            window.close()


if __name__ == "__main__":
    main = main()
    main.on_enable()
    main.on_disable()
