import PySimpleGUI as sg

from ui.UI import UI

"""
Summary: This class is the main body layout of the GUI
"""


class Admin(UI):

    # initiate the layout
    def __init__(self):
        title = [
            [sg.Text("Administrator Use ONLY", font=("Helvetica", 25), size=(30, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Search for:", size=(10, 1), background_color="white", text_color="black"), sg.Radio('Invoice', "RADIO1", default=True, size=(7,1),text_color="black", background_color="white", key="_AD_INV_RAD_"),sg.Radio('Packing list', "RADIO1", default=False, size=(10,1),text_color="black",  background_color="white", key="_AD_PKL_RAD_")],
            [sg.Text("Search by:", size=(10, 1), background_color="white", text_color="black"),sg.InputCombo(('Condition 1', 'Condition 2'), size=(23, 1), key="_AD_SCB_IPC_")],
            [sg.Text("Key words:", size=(10, 1), background_color="white", text_color="black"),sg.InputText(key="_AD_KEY_IP_", size=(25, 1), enable_events=True), sg.Button("Search",size=(10, 1), key="_AD_SEARCH_BTN")],
            [sg.Listbox(values=["value1", "value2", "value3"],size=(50, 15), enable_events=True, key='_AD_RST_LST_')]
        ]

        buttons = [
            [sg.Button("User Group Management", pad=(30, 1), size=(20, 1), button_color=("black", "light gray"), key="_AD_UGM_BTN_"), sg.Button("Quit", pad=(20,1),size=(20, 1), button_color=("black", "light gray"), key="_AD_QUIT_BTN_")]
        ]

        column_all = [
            [sg.Column(title, background_color="white", key="_AD_TITL_", justification="center")],
            [sg.Column(column1, background_color="white", key="_AD_COLUMN_1_", justification="center")],
            [sg.Column(buttons, pad=(10, 50), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(20, 10), background_color="white")]
        ]

