import PySimpleGUI as sg

"""
Summary: This class is the main body layout of the GUI
"""


class Client(object):
    # private element, shouldn't be changed from outside
    _layout = []

    # initiate the layout
    def __init__(self):
        save_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////z++7H7LOG1llrzDRnyy9jyipqzDOR2mnK7bfx+uzi9deI1lyE1Vfe9NLw+uuF1Vjv+uq86KRlyy3A6amM2GFozDBtzjhozDGV226s442w5JSp4oqU223B6qv7/vr8/vvz++/w+ur+//77/vm86KNnyzCb3XfD6q1800zH7LL8/vqf3n3b8s7s+OTt+ebS8MLk9trn999yzz6C1FSE1ViC1VV30UV70kuD1VVkyix30UaD1VZtzThmyy550Uh9003I7LT4/fV+00+J117d89H2/PPu+ef1+/Ho9+Cj4IGp4ol60klwzjzY8sry++50z0FszTa05pjs+eXp9+Hy++3Q77+J1133/PSi4IDm9tx00EHp+OCA1FF80030+/Dd89CM2GL5/fbM7biv45H9/v3B6qqg337R78BrzTSV22/l9tv4/PXy+u3M7rmo4Yil4ISy5ZWv5JHM7rp50ki66KFwzz120ET6/fiL12BqzTTZ8sv+//35/ffE669tzTeW23C355zV8cWy5Zaa3Xa96aVpzDOd3XnL7bj4/fax5ZWR2WiY3HK3553///625pvX8chuzjms4o2P2We4557X8cne9NGv5JL3/PXn997m9t3D6qyF1lnd9NFwzzz8/vzl9tzA6qmB1FSf3nyn4Yf9/vyR2mj6/fm05ZiS2mppzDK756J/01Cq4oqz5Zf1/PGZ3HOk4ILf9NNszTfk9tvv+ul00EK555/v+ejJ7bXp+OHq+OJrzTVkyit10EOo4oiq4ovs+eaN2GOc3nfW8cdzz0Dv+emH1lvs+OWg332+6ab2/PLV8cbK7bjV8cdxzz2s446T22u15pvN7rvu+eh20USG1lqB1FPb882B1FK+6afx+usAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABABAyZwAGAwgTKlzIsKHDhxAjSpxIsaJFiRjCzBEiEACtARdDihxJsqRJil1oAXgC8qTLlzBjuuzyJJTMmzhz6kwYquXOn0CDVjwotKhRo0SPKl3KtKnTp1CjSp1KtarVnNHevFH0JszVr0pDdXwiMBDYs0AJAQh1B+EQFQAIoZ2Ls8UThk/m0N0LcwEViXfuDOjSpS3CO10aCk6KuMsAw3ypqhACueGAFiu5AOAi18AbAJUNYLD7R3SgJ6hRz6ETeSqElW+SLuTyhOgdzYnvCGmxcAAAvZ7XJlTbQnZrp2GoCMn7BsJCQj4NbADwRvQc0ApDCTl4B4CKhdOjH/93imGIXYEqjCuMBsCsAbXuET7hLT0uQ+HjqRLauEHhnWiEBPgIAI8ghMF8RH3W0hxPPEIIgAGyB1x+VGGW0BtkUbGAXwD0h5B2LXGxAFFwbWiiiTZRyNQQ6qmF0GcTGhAGgQo9YZZaHhogllcqTgWABAwNiNACxlT2WY4GTGZAIAAkxd4ZPU7VAmVJHbjAkE84ZyBmSM74SF4LGUOFbAcOEaVSQyzgnVYSCGFMHggRstsbhLyxAJcKjUYFdgoNYYwxDhIiVnFnKoXBHMZ0NIdsEOwJm5cLDaoYgwI9QYh6hWaq6aacdurpp1GyBmqmdMQ3apSniXfqeHSQ1YKoq44Md9lYbMUa2R2nCRQQADs="

        title = [
            [sg.Text("Create New Client Information", font=("Helvetica", 15), size=(20, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Client Telephone Number:", font=("arial", 10), background_color="white", text_color="black"),sg.InputText(key="_CP_PHONE_IP_", size=(25, 1), enable_events=True)]
        ]

        column2 = [
            [sg.Text("Client Name: ",font=("arial", 10), background_color="white", text_color="black"),sg.InputText(key="_CP_NAME_IP_", size=(25, 1), enable_events=True)]
        ]

        column3 = [
            [sg.Text("Client Address: ", font=("arial", 10), background_color="white", text_color="black"),
             sg.InputText(key="_CP_ADDRESS_IP_", password_char="*", size=(25, 1), enable_events=True)]
        ]

        buttons = [
            [sg.Button(image_data=save_btn_ioc,border_width=0, size=(20, 1), button_color=("black", "light gray"), key="_CP_SAVE_BTN_"),
            sg.Button(image_data=save_btn_ioc, border_width=0, size=(20, 1), button_color=("black", "light gray"),
                       key="_CP_CANCEL_BTN")]
        ]

        column_all = [
            [sg.Column(title, background_color="white", key="_CP_TITLE_COLUMN_",  justification="center")],
            [sg.Column(column1, background_color="white", key="_CP_PHONE_COLUMN_",pad=(10,10), justification="center")],
            [sg.Column(column2, background_color="white", key="_CP_NAME_COLUMN_",pad=(10,10), justification="center")],
            [sg.Column(column3, background_color="white", key="_CP_ADDRESS_COLUMN_", pad=(10, 10), justification="center")],
            [sg.Column(buttons, pad=(10, 20), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(20, 10), background_color="white", justification="center")]
        ]

    # outside method can get the layout by this method
    def get_layout(self):
        return self._layout