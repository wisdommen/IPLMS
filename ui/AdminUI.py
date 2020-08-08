import PySimpleGUI as sg

from ui.AbstractUI import UI
from utils.Utils import make_table

"""
Summary: This class is the main body layout of the GUI
"""


class Admin_UI(UI):

    # initiate the layout
    def __init__(self):
        self.header_list = ["Invoice No.", "Client Name", "Date", "Goods description"]
        self.conditions = ["Invoice No.(ASC)", "Client Name(ASC)", "S/C No.(ASC)", "Date(ASC)", "Destination port(ASC)",
                           "Goods description(ASC)", "Net weight(ASC)", "Bags(ASC)", "Quantity(ASC)",
                           "Total Measurement(ASC)", "Invoice No.(DESC)", "Client Name(DESC)", "S/C No.(DESC)",
                           "Date(DESC)", "Destination port(DESC)", "Goods description(DESC)", "Net weight(DESC)",
                           "Bags(DESC)", "Quantity(DESC)", "Total Measurement(DESC)"]
        self.data_list = []
        self.data = make_table(1, len(self.header_list), self.data_list)

        title = [
            [sg.Text("Administrator Use ONLY", font=("Helvetica", 25), size=(30, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Search for:", size=(10, 1), background_color="white", text_color="black"),
             sg.Radio('Invoice', "RADIO1", default=True, size=(7, 1), text_color="black", background_color="white",
                      key="_AD_INV_RAD_"),
             sg.Radio('Packing list', "RADIO1", default=False, size=(10, 1), text_color="black",
                      background_color="white", key="_AD_PKL_RAD_")],
            [sg.Text("Search by:", size=(10, 1), background_color="white", text_color="black"),
             sg.InputCombo(values=self.conditions, size=(23, 1), key="_AD_SCB_IPC_")],
            [sg.Text("Key words:", size=(10, 1), background_color="white", text_color="black"),
             sg.InputText(key="_AD_KEY_IP_", size=(25, 1), enable_events=True),
             sg.Button("Search", size=(10, 1), key="_AD_SEARCH_BTN_")]
        ]

        table = [
            [sg.Table(values=self.data, bind_return_key=True, key="_AD_RET_TABLE_", justification="center",
                      headings=self.header_list, auto_size_columns=False, alternating_row_color='blue',
                      num_rows=20, col_widths=[10, 10, 15, 20], enable_events=True)]
        ]

        buttons2 = [
            [sg.Button("Open by Excel", pad=(10, 1), size=(13, 1), button_color=("black", "light gray"),
                       key="_AD_OPEN_BTN_"),
             sg.Button("Edit", pad=(10, 1), size=(13, 1), button_color=("black", "light gray"), key="_AD_EDIT_BTN_"),
             sg.Button("Delete", pad=(10, 1), size=(13, 1), button_color=("black", "light gray"), key="_AD_DEL_BTN_")]
        ]

        buttons = [
            [sg.Button("User Group Management", pad=(20, 1), size=(20, 1), button_color=("black", "light gray"),
                       key="_AD_UGM_BTN_", disabled=True),
             sg.Button("Quit", pad=(20, 1), size=(20, 1), button_color=("black", "light gray"), key="_AD_QUIT_BTN_")]
        ]

        column_all = [
            [sg.Column(title, background_color="white", key="_AD_TITL_", justification="center")],
            [sg.Column(column1, background_color="white", key="_AD_COLUMN_1_", justification="center")],
            [sg.Column(table, background_color="white", justification="center")],
            [sg.Column(buttons2, pad=(10, 10), background_color="white", justification="center")],
            [sg.Column(buttons, pad=(10, 50), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(20, 10), background_color="white")]
        ]

    def set_table(self, header_list, data_list):
        self.header_list = header_list
        self.data_list = data_list

    def get_need_validate_fields(self) -> map:
        return {}
