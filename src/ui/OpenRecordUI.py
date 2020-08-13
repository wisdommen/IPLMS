import PySimpleGUI as sg

from src.ui.AbstractUI import UI
from src.utils.Utils import make_table

"""
Summary: This class is the main body layout of the GUI
"""


class OpenRecord_UI(UI):

    # initiate the layout
    def __init__(self, row: int, col: int, data_list: list, header_list: list):
        super().__init__()
        data = make_table(row, col, data_list)

        buttons = [
            [sg.Button("Load", pad=(20, 1), size=(20, 1), button_color=("black", "light gray"),
                       key="_OR_OPEN_BTN_", tooltip="Load the record to fields"),
             sg.Button("Delete", pad=(20, 1), size=(20, 1), button_color=("black", "light gray"), key="_OR_DEL_BTN_",
                       tooltip="Delete the record"),
             sg.Button("Cancel", pad=(20, 1), size=(20, 1), button_color=("black", "light gray"), key="_OR_CAN_BTN_",
                       tooltip="Delete the record")]
        ]

        column_all = [
            [sg.Table(data, bind_return_key=True, key="_OR_TABLE_", justification="center",
                      headings=header_list, auto_size_columns=True, alternating_row_color='blue')],
            [sg.Column(buttons, pad=(10, 20), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Text("Double click or use \"Open\" button to load the record to fields", background_color="white",
                     text_color="black")],
            [sg.Column(column_all, pad=(20, 10), background_color="white", justification="center")]
        ]

    # Overriding method
    def get_need_validate_fields(self) -> map:
        # documentation see abstract class
        return {}
