#############
# INTRODUCTION
# Programmer: Isaac Bao
# Client: MF Gas Company
# Program: Gas Bill Calculator
# Purpose: To show the total charge of user's Gas usage
# Input: Keyboard
# Input data: Customer Name; Bill date; Usage
# Processing: Key algorithm(s)
# Output: Screen
# Output Information: Company name; Bill type; Payment duration; Bill date; Customer name; Usage; Usage charge;
#                     Supply charge; Total charge;
# Internal storage: Memory, Hard drive
# External storage: None
#############
from logic.Login import Login
from main.MainApplication import MainApplication

import PySimpleGUI as sg

from utils import Config


class main(MainApplication):

    def on_enable(self):

        # load config, if no config found, create a new one
        if not Config.is_config_exists():
            Config.save_default_config()
        config = Config.get_config()

        # if use database (developing)
        if config["enable_database"]=="true":
            print("connecting to the database...")
            print("")
            pass

        # set up login page
        login = sg.Window("IPLMS - Login", self.login_ui.get_layout(), auto_size_buttons=False, background_color="lightgray",
                          no_titlebar=True, grab_anywhere=True, size=(300, 300), use_default_focus=True, border_depth=1)
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
                            financial = self.create_window("financial","IPLMS - Invoice Generator", self.financial_ui.get_layout())
                            event3 = ""
                            while event3 is not None:
                                event3, values3 = financial.read(timeout=300)
                                print(event3, values3)
                                if event3 == "_PL_NEW_BTN_":
                                    client = self.create_window("client","IPLMS", self.client_ui.get_layout(), disable_close=True)
                                    client.un_hide()
                                    event4, values4 = client.read()
                                    print(event4, values4)
                                    if event4 == "_CP_SAVE_BTN_":
                                        client.hide()
                                    elif event4 == "_CP_CANCEL_BTN":
                                        client.hide()
                                elif event3 == "_FA_QUIT_BTN_" or event3 is None:
                                    break
                            break
                        elif department == "packing":
                            packing = self.create_window("packing","IPLMS - Packing List Generator", self.packing_ui.get_layout())
                            event2 = ""
                            while event2 is not None:
                                event2, values2 = packing.read()
                                print(event2, values2)
                                if event2 == "_PL_NEW_BTN_":
                                    client = self.create_window("client","IPLMS", self.client_ui.get_layout(), disable_close=True)
                                    client.un_hide()
                                    event4, values4 = client.read()
                                    print(event4, values4)
                                    if event4 == "_CP_SAVE_BTN_":
                                        client.hide()
                                    elif event4 == "_CP_CANCEL_BTN":
                                        client.hide()
                                elif event2 == "_PL_QUIT_BTN_" or event2 is None:
                                    break
                            print(event2, values2)
                            break
                        elif department == "admin":
                            admin = self.create_window("admin", "Invoice and Packing List Management System", self.admin_ui.get_layout())
                            event5 = ""
                            while event5 is not None:
                                event5, values5 = admin.read(timeout=200)
                                print(event5, values5)
                                if event5 == "_AD_UGM_BTN_":
                                    user_manage = self.create_window("user_manage", "IPLMS", self.user_manage_ui.get_layout(), disable_close=True)
                                    user_manage.un_hide()
                                    event6 = ""
                                    while event6 is not None:
                                        event6, values6 = user_manage.read()
                                        print(event6, values6)

                                        if event6 == "_UM_SAVE_BTN_":
                                            user_manage.hide()
                                            break
                                        elif event6 == "_UM_QUIT_BTN_":
                                            user_manage.hide()
                                            break
                                        elif event6 == "_UM_CREATE_BTN_":
                                            new_user = self.create_window("new_user", "IPLMS", self.new_user_ui.get_layout(), disable_close=True)
                                            new_user.un_hide()
                                            new_user.bring_to_front()
                                            event7, values7 = new_user.read()
                                            print(event7, values7)
                                            if event7 == "_NU_CREATE_BTN_":
                                                new_user.hide()
                                            elif event7 == "_NU_CANCEL_BTN":
                                                new_user.hide()
                                elif event5 == "_AD_QUIT_BTN_":
                                    break

                            print(event5, values5)
                            break
                    else:
                        print(passport)
            # "X" on the windows top was pressed
            elif event == "_LG_CROSS_":
                break

    def on_disable(self):
        for each_data in self.data.keys():
            if each_data.save_data(self.data[each_data]) is False:
                print("Permission error")
        for each in self.windows_map.keys():
            window = self.windows_map[each]
            window.close()


if __name__ == "__main__":
    main = main()
    main.on_enable()
    main.on_disable()

##############
# JUSTIFICATION
# Provide justifications against a plausible alternative for the following
# -Variable types
# 1. String type for Date
#    1. I choose string type because I need to split them and make validation.
#    2. I don't choose other types, because they cannot use split method
# 2. String type for user name
#    1. Because there is no other type I can use to display name(string)
# 3. Int type for Usage
#    1. Because the usage is asked to be round to nearest whole number before calculating
# 3. Float type for Usage Charge,Supply Charge and Total Charge
#    1. Because most of time usage is not a whole number
#    2. If I choose int type, there will be not accurate.
# -Processing algorithms
#    If the usage is not over 2000 MJ, the charge will count as usage times 0.0346 and plus 2 months' supply fee.
#    if the usage is over 2000 kL, the charge will count as usage times 0.0401 and plus 2 months' supply fee.
# -Validation techniques
#    Date:
#       Date should not less than 1 or more than 31 or 30 depends on the Month
#       Month should not less than 1 or more than 12
#       Year should not less than 1000
#   Name:
#       Name should only contain letters and space
#       Name should not only have spaces
#   Usage:
#       Usage should only be POSITIVE numbers
# -Output format, including:
# --Layout of output text
# ---Use "-------------------" to split different section of the bill will make the bill has a high readability which
#    other ways of split can't
# --Text formatting technique employed in the print function
# ---Round the number in the display to 2 decimal places increase the accurate of the result, if only round to the whole
#    number will make the bill not accurate, except the Usage display because Usage is asked to round to the whole
#    number before calculating.
# ---The spaces before result numbers will increase the readability, otherwise user will be difficult to read results
# --GUI design choices: UI control, layout, size, position, colour etc.
# ---layout:
# ----Put the question text and the input in a column and put them in a line and I put all the column in a big column.
# ----The reason I do this is because this will make all the elements in a same justification and this will make the
# ----future maintain easy. Otherwise, in the future maintains will be very difficult to adjust all elements, such
# ----as move all of them to another position or adjust the size for all elements. I set user can not adjust the window
# ----size, this will prevent the user form changing the size of the windows and make the layout of all elements become
# ----a mass which decrease the clarity and readability.
# ---size:
# ----the size of text, able are all auto-sized. Because it will save a lot of time, I don't need to adjust all the
# ----text size, otherwise, I will spend a lot of time on changing the text size. I adjust the button manually, because
# ----the auto-size of the button is too small.
# ---color:
# ----I changed the default color of buttons, because they will change the color to white when click on it, with white
# ----text on it will make the text hard to read. Therefore, I changed it to white background with black text and change
# ----to light gray when click on it. I changed the background color of the window which default wis blue to meet the
# ----enquiry. I decided to use orange background and red text in my error message box which will increase the
# ----importance level of the message, and white background and black text in the info message box which is not
# ----important, and white background and red text in the warning message box which needs to be take care but not
# ----urgent.
##############
