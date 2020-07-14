import PySimpleGUI as sg

"""
Summary: This class is the main body layout of the GUI
"""


class Financial(object):
    # private element, shouldn't be changed from outside
    _layout = []

    # initiate the layout
    def __init__(self):
        new_client_ioc = b"R0lGODlhFwAVAHAAACwAAAAAFwAVAIH///8AqPMAAAAAAAACPYQfmcfdCp00sM5X7aU5btB5W6h8IBlwi0MiJbN0oJq6cVSK2fieLQpMBVG+4c4YwqyKwKIt6KQ1dcYooAAAOw=="
        calendar_ico = b"R0lGODlhFQAUAHAAACwAAAAAFQAUAIL///8AqPP7/PdNyP981v/2/vwAAAAAAAADSAgK0fstvNWGg8HK6cimBPNpXWSGZip5Kqq+cCzDFGQrZq3jVLQzN9Fs+PsAcT5esXc5Kp+5p9M5rC530anxk90uBNxMVTVIAAA7"

        title = [
            [sg.Text("Financial Use ONLY", font=("Helvetica", 25),size=(20, 1), background_color="white", text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Client information:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.InputCombo(('Client 1', 'Client 2'), size=(19, 1)), sg.Button("", font=("Helvetica", 8),size=(4, 1), button_color=("black", "light gray"), key="_PL_NEW_BTN_",border_width=0, image_data=new_client_ioc, tooltip="Add a new client")],
            [sg.Text("Invoice No.:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.InputText(key="_FA_INV_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("S/C No.:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.InputText(key="_FA_SC_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("Date and Time:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.InputText(key="_FA_DATE_IP_", size=(21, 1), enable_events=True), sg.CalendarButton('', font=("Helvetica", 8), size=(5, 1), target=(3,1), key="_FA_DATE_PICKER_", border_width=0, image_data=calendar_ico, tooltip="Choose a date")]
        ]

        column2 = [
            [sg.Text("Destination port: ", size=(15, 1), background_color="white", text_color="black", justification="center"),
            sg.InputText(key="_FA_DES_PORT_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("Goods Description:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.InputText(key="_FA_GOODS_DES_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("Unit Price/AUD:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.Spin(values=[i for i in range(1, 10000)],size=(23,1), initial_value='1000')],
            [sg.Text("Quantity/TON:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.Spin(values=[i for i in range(1, 1000)],size=(23,1), initial_value='20')]
        ]

        buttons = [
            [sg.Button("Clear All", size=(20, 1), button_color=("black", "light gray"), key="_FA_CLA_BTN_"),
             sg.Button("Save", size=(20, 1), button_color=("black", "light gray"), key="_FA_SAVE_BTN_"),
             sg.Button("Quit", size=(20, 1), button_color=("black", "light gray"), key="_FA_QUIT_BTN_")]
        ]

        column_all = [
            [sg.Column(title, pad=(10,10), background_color="white", key="_FA_TITL_COLUMN_", justification="center")],
            [sg.Column(column1,pad=(20,10), background_color="white", key="_FA_COLUMN_1_"), sg.Column(column2,pad=(20,10), background_color="white", key="_FA_COLUMN_2_")],
            [sg.Column(buttons, pad=(10, 30), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(10, 10), background_color="white")]
        ]

    # outside method can get the layout by this method
    def get_layout(self):
        return self._layout
