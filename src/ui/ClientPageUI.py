import PySimpleGUI as sg

from src.ui.AbstractUI import UI

"""
Summary: This class is the main body layout of the GUI
"""


class Client_UI(UI):

    # initiate the layout
    def __init__(self):
        super().__init__()
        save_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////z++7H7LOG1llrzDRnyy9jyipqzDOR2mnK7bfx+uzi9deI1lyE1Vfe9NLw+uuF1Vjv+uq86KRlyy3A6amM2GFozDBtzjhozDGV226s442w5JSp4oqU223B6qv7/vr8/vvz++/w+ur+//77/vm86KNnyzCb3XfD6q1800zH7LL8/vqf3n3b8s7s+OTt+ebS8MLk9trn999yzz6C1FSE1ViC1VV30UV70kuD1VVkyix30UaD1VZtzThmyy550Uh9003I7LT4/fV+00+J117d89H2/PPu+ef1+/Ho9+Cj4IGp4ol60klwzjzY8sry++50z0FszTa05pjs+eXp9+Hy++3Q77+J1133/PSi4IDm9tx00EHp+OCA1FF80030+/Dd89CM2GL5/fbM7biv45H9/v3B6qqg337R78BrzTSV22/l9tv4/PXy+u3M7rmo4Yil4ISy5ZWv5JHM7rp50ki66KFwzz120ET6/fiL12BqzTTZ8sv+//35/ffE669tzTeW23C355zV8cWy5Zaa3Xa96aVpzDOd3XnL7bj4/fax5ZWR2WiY3HK3553///625pvX8chuzjms4o2P2We4557X8cne9NGv5JL3/PXn997m9t3D6qyF1lnd9NFwzzz8/vzl9tzA6qmB1FSf3nyn4Yf9/vyR2mj6/fm05ZiS2mppzDK756J/01Cq4oqz5Zf1/PGZ3HOk4ILf9NNszTfk9tvv+ul00EK555/v+ejJ7bXp+OHq+OJrzTVkyit10EOo4oiq4ovs+eaN2GOc3nfW8cdzz0Dv+emH1lvs+OWg332+6ab2/PLV8cbK7bjV8cdxzz2s446T22u15pvN7rvu+eh20USG1lqB1FPb882B1FK+6afx+usAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABABAyZwAGAwgTKlzIsKHDhxAjSpxIsaJFiRjCzBEiEACtARdDihxJsqRJil1oAXgC8qTLlzBjuuzyJJTMmzhz6kwYquXOn0CDVjwotKhRo0SPKl3KtKnTp1CjSp1KtarVnNHevFH0JszVr0pDdXwiMBDYs0AJAQh1B+EQFQAIoZ2Ls8UThk/m0N0LcwEViXfuDOjSpS3CO10aCk6KuMsAw3ypqhACueGAFiu5AOAi18AbAJUNYLD7R3SgJ6hRz6ETeSqElW+SLuTyhOgdzYnvCGmxcAAAvZ7XJlTbQnZrp2GoCMn7BsJCQj4NbADwRvQc0ApDCTl4B4CKhdOjH/93imGIXYEqjCuMBsCsAbXuET7hLT0uQ+HjqRLauEHhnWiEBPgIAI8ghMF8RH3W0hxPPEIIgAGyB1x+VGGW0BtkUbGAXwD0h5B2LXGxAFFwbWiiiTZRyNQQ6qmF0GcTGhAGgQo9YZZaHhogllcqTgWABAwNiNACxlT2WY4GTGZAIAAkxd4ZPU7VAmVJHbjAkE84ZyBmSM74SF4LGUOFbAcOEaVSQyzgnVYSCGFMHggRstsbhLyxAJcKjUYFdgoNYYwxDhIiVnFnKoXBHMZ0NIdsEOwJm5cLDaoYgwI9QYh6hWaq6aacdurpp1GyBmqmdMQ3apSniXfqeHSQ1YKoq44Md9lYbMUa2R2nCRQQADs="
        cancel_btn_ioc = b"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"
        menu_def = [
            ['Edit', ['Open']],
        ]

        title = [
            [sg.Text("Create New Client Information", font=("Helvetica", 15), size=(25, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Client ID:", font=("arial", 10), background_color="white", text_color="black",
                     justification="right")],
            [sg.Text("Client Telephone Number:", font=("arial", 10), background_color="white", text_color="black",
                     justification="right")],
            [sg.Text("Client Name: ", font=("arial", 10), background_color="white", text_color="black",
                     justification="right")],
            [sg.Text("Client Address: ", font=("arial", 10), background_color="white", text_color="black")]
        ]

        column2 = [
            [sg.Text("", font=("arial", 10), size=(25, 1), background_color="white", text_color="black",
                     justification="left", key="_CLIENT_ID_")],
            [sg.InputText(key="_CP_PHONE_IP_", size=(25, 1))],
            [sg.InputText(key="_CP_NAME_IP_", size=(25, 1))],
            [sg.InputText(key="_CP_ADDRESS_IP_", size=(25, 1))]
        ]

        buttons = [
            [sg.Button(image_data=save_btn_ioc, border_width=0, size=(20, 1), button_color=("black", "light gray"),
                       key="_CP_SAVE_BTN_"),
             sg.Button(image_data=cancel_btn_ioc, border_width=0, size=(20, 1), button_color=("black", "light gray"),
                       key="_CP_CANCEL_BTN_")]
        ]

        column_all = [
            [sg.Column(title, background_color="white", key="_CP_TITLE_COLUMN_", justification="center")],
            [sg.Column(column1, background_color="white", key="_CP_PHONE_COLUMN_", pad=(10, 10), justification="left"),
             sg.Column(column2, background_color="white", key="_CP_NAME_COLUMN_", pad=(10, 10), justification="right")],
            [sg.Column(buttons, pad=(10, 20), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Menu(menu_def, )],
            [sg.Column(column_all, pad=(20, 10), background_color="white", justification="center")]
        ]

    # Overriding method
    def get_need_validate_fields(self):
        # documentation see abstract class
        return {
            "_CP_PHONE_IP_": "[^0-9 +]",
            # only tell the validator to validate the name by its own way, so no rule apply here
            # or any rule here, does not matter.
            "_CP_NAME_IP_": ""
        }
