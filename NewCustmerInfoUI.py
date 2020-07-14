import PySimpleGUI as sg

"""
Summary: This class is the main body layout of the GUI
"""


class Login(object):
    # private element, shouldn't be changed from outside
    _layout = []

    # initiate the layout
    def __init__(self):
        column1 = [
            [sg.Text("Username:", size=(20, 1), background_color="white", text_color="black")],
            [sg.InputText(key="_USERNAME_", size=(25, 1), enable_events=True)]
        ]

        column2 = [
            [sg.Text("Password: ", size=(20, 1), background_color="white", text_color="black")],
            [sg.InputText(key="_PASSWORD_", size=(25, 1), enable_events=True)]
        ]

        buttons = [
            [sg.Button("Login", size=(20, 1), button_color=("black", "light gray"), key="_LOGIN_")]
        ]

        column_all = [
            [sg.Column(column1, background_color="white", key="_NAME_COLUMN_")],
            [sg.Column(column2, background_color="white", key="_DATE_COLUMN_")],
            [sg.Column(buttons, pad=(10, 50), background_color="white")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(20, 10), background_color="white")]
        ]

    # outside method can get the layout by this method
    def get_layout(self):
        return self._layout