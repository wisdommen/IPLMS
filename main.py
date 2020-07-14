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
import PySimpleGUI as sg

from LoginUI import Login, MessageBox
from FinancialUI import Financial
from PackingUI import Packing
from AdminUI import Admin

# instantiate UI objects
login_ui = Login()
financial_ui = Financial()
packing_ui = Packing()
admin_ui = Admin()
mg = MessageBox()

# instantiate window object


login = sg.Window("IPLMS - Login", login_ui.get_layout(), auto_size_buttons=False,
                  background_color="white", no_titlebar=True, grab_anywhere=True, size=(1, 1), use_default_focus=True)


def financial_thread():
    financial = sg.Window("IPLMS - Invoice Generator", financial_ui.get_layout(), auto_size_buttons=False,
                          finalize=True,
                          background_color="white")
    event3, values3 = financial.read()
    while event3 is not None:
        event3, values3 = financial.read()
    login.close()
    financial.close()


def packing_thread():
    packing = sg.Window("IPLMS - Invoice Generator", packing_ui.get_layout(), auto_size_buttons=False, finalize=True,
                        background_color="white")
    event2, values2 = packing.read()
    while event2 is not None:
        event2, values2 = packing.read()
    login.close()
    packing.close()


def admin_thread():
    admin = sg.Window("Invoice and Packing List Management System", admin_ui.get_layout(), auto_size_buttons=False,
                      finalize=True, background_color="white")
    admin.hide()


# Main loop for the Gui window
while True:

    event, values = login.read(timeout=10)

    if values["_USERNAME_"] != "":
        login.FindElement("_USERNAME_")
    else:
        login.grab_any_where_on()

    event, values = login.read(timeout=300)

    print(event, values)

    if event != "_LG_CROSS_":
        if event == "_LOGIN_":
            login.hide()
            if "1" in values.values():
                financial = sg.Window("IPLMS - Invoice Generator", financial_ui.get_layout(), auto_size_buttons=False,
                                      finalize=True,
                                      background_color="white")
                event3, values3 = financial.read()
                print(event3, values3)
                while event3 is not None:
                    event3, values3 = financial.read()
                    print(event3, values3)
                print(event3, values3)
                login.close()
                financial.close()
                break
            elif "2" in values.values():
                packing = sg.Window("IPLMS - Invoice Generator", packing_ui.get_layout(), auto_size_buttons=False,
                                    finalize=True,
                                    background_color="white")
                event2, values2 = packing.read()
                print(event2, values2)
                while event2 is not None:
                    event2, values2 = packing.read()
                    print(event2, values2)
                print(event2, values2)
                login.close()
                packing.close()
                break
            else:
                admin = sg.Window("Invoice and Packing List Management System", admin_ui.get_layout(),
                                  auto_size_buttons=False,
                                  finalize=True, background_color="white")
                event4, values4 = admin.read()
                print(event4, values4)
                while event4 is not None:
                    event4, values4 = admin.read()
                    print(event4, values4)
                print(event4, values4)
                login.close()
                admin.close()
                break
    # "X" on the windows top was pressed
    else:
        break

login.close()

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
