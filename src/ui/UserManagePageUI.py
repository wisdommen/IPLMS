import PySimpleGUI as sg

from src.ui.AbstractUI import UI

"""
Summary: This class is the main body layout of the GUI
"""


class UserMange_UI(UI):

    """
        This class is not going to be completed due to the time constrain, but the reason I keep it here
        is I want to complete this in the future, please ignore everything in this class
    """

    # initiate the layout
    def __init__(self):
        super().__init__()
        title = [
            [sg.Text("User Groups Management", font=("Helvetica", 25), size=(30, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Listbox(values=["value1", "value2", "value3"], size=(50, 15), enable_events=True, key='_AD_RST_LST_')]
        ]

        buttons = [
            [sg.Button("Create a new user group", pad=(30, 10), size=(47, 1), button_color=("black", "light gray"),
                       key="_UM_CREATE_BTN_")],
            [sg.Button("Save", pad=(30, 10), size=(20, 1), button_color=("black", "light gray"), key="_UM_SAVE_BTN_"),
             sg.Button("Quit", pad=(20, 1), size=(20, 1), button_color=("black", "light gray"), key="_UM_QUIT_BTN_")]
        ]

        column_all = [
            [sg.Column(title, background_color="white", key="_UM_TITL_", justification="center")],
            [sg.Column(column1, background_color="white", key="_UM_COLUMN_1_", justification="center")],
            [sg.Column(buttons, pad=(10, 50), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(20, 10), background_color="white")]
        ]

    # Overriding method
    def get_need_validate_fields(self):
        # documentation see abstract class
        return {}
