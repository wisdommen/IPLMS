import PySimpleGUI as sg

from ui.AbstractUI import UI

"""
Summary: This class is the main body layout of the GUI
"""


class Financial_UI(UI):
    # initiate the layout
    def __init__(self):
        new_client_ioc = b"R0lGODlhFwAVAHAAACwAAAAAFwAVAIH///8AqPMAAAAAAAACPYQfmcfdCp00sM5X7aU5btB5W6h8IBlwi0MiJbN0oJq6cVSK2fieLQpMBVG+4c4YwqyKwKIt6KQ1dcYooAAAOw=="
        calendar_ico = b"R0lGODlhFQAUAHAAACwAAAAAFQAUAIL///8AqPP7/PdNyP981v/2/vwAAAAAAAADSAgK0fstvNWGg8HK6cimBPNpXWSGZip5Kqq+cCzDFGQrZq3jVLQzN9Fs+PsAcT5esXc5Kp+5p9M5rC530anxk90uBNxMVTVIAAA7"
        clear_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////3+v3Q4vORvONlodhin9dbm9VtptqEtN++1+/1+fzt9PqMueKAst7q8vry9/yJt+F+sN620ux7r91gnteszOrW5vSBst9endaOuuLU5fTn8Pnu9fvp8vnT5PSdw+a+2O7z+Pxhntbf6/f9/v/6/P7b6fbc6vbg7Pf4+/18r95koNfh7fj8/f7T5fRjoNd4rdzN4PJ2rNzS4/TS5PN5rdzM4PHy+Pyix+dxqNp8r9291+6GteBxqduDs9+Cs999sN5sptlzqtt/sd5qpNlcm9V1q9y+1+7S5PSAst/O4fLr8/rx9/u/2O9modiXwOTV5fTx9vvx9vzw9vu41O1xqNtcnNXl7/jY5/Xb6fX+//+61e6ItuG00eyjx+ekx+e20+zZ6PV2q9zi7vjm8Pmwz+uixuenyei51O3e6/bV5vSoyumSvePn8fn+/v9fndbX5vWlyOi10uxyqduPu+La6PWFteDn8Pjv9fve6/dnotj0+fxfntZdnNbC2u+LuOGtzephn9f2+v3A2e/j7veHtuD7/P6NueKZweX5+/3u9PvX5/VspdmfxOfB2u9oo9jC2fC20u3d6vbM4PJ+sd7o8fn5/P6It+DC2vD5+/671e5rpdnP4vPH3fFkodeTveOexOary+n0+PxdnNXa6fbA2O/7/f7j7vifxebh7Pd3rNyDtN/J3vHi7ffI3fGAsd9spdqz0eza6Pavz+t7rt3d6vevzut0qtvv9vvh7ffk7/js9Pquzurs8/qxz+vp8fnl7/nG3PDR4/PF2/CbwuW71u7E2/CaweWKuOGhxuevzupup9rb6vaz0OuszekAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABALjBgsGmAgYSKlzIsKHDhxAjSpxIsaLFixI3XQIhUOCNSxhDihxJsqTJimJuDAR5sqXLlzBbigEQKabNmzhzKqwgRqfPn0AvikEYtKhRo0SPKl3KtKnTp1CjSp16tIKLnlSzBr3kgoWir5MQMeTIUqtZnCwEsrDBIi2ASVgNgFBU9qxdl2knMdxkA4ANrCA+3h18UpZfh2Js3GiUMHBdwpAtblIEIC7DjT4a38i8cJMYMZc+J1X4GbRohp8NlLYcGShHGxUdLxTjFQBlRSDiFkDk9YbKGyA2LVT0kYVKKK2Npq1JMRIAzgYuGa/Q6FOjCgSx0mZBHVGFviCSev9dS/1xcp1pWUOcW1bWjQoLCziHr7pCXdqKoKdNo/68T8oWyRadIiyMptoNaURElkJp0edfUWkFuFlCzkVi4CZp5AeRc2VR1t+DOVEmVnMAsOScImmkAYWKKQ70SUKbIAKCDStCQVlZaQAgAohFgRebhgY4l+KQKdqQxl+q5fjVkMSVdYeOPAZVAQAJUiRghaOJoKUIBSTmlxg7JjSlk1BGCZRKH0r3olx0iemXgQv5gCJrzkH3ZJhm+nQinD6ksZhm0OXImhhpgGCAnLApJMIlT5L5SJ5AKcafGJt4dkmOFQjHZllT3lHaJn0CAB+hivD02SWKlahQjnhCqlMkt7FqkCGKPCkUGHQGnEFZGnfMSp8InzzZa4Y29NVhma76dEkFM4IAQq0LfZIbQ59EYsOMFayZ0KLWghDJJ6BFEtd3rSYLabnmppvch+rmKYah7ao7JbvxPniJQIrQW29rm7glkIX7gigGdgIFBAA7"
        save_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////z++7H7LOG1llrzDRnyy9jyipqzDOR2mnK7bfx+uzi9deI1lyE1Vfe9NLw+uuF1Vjv+uq86KRlyy3A6amM2GFozDBtzjhozDGV226s442w5JSp4oqU223B6qv7/vr8/vvz++/w+ur+//77/vm86KNnyzCb3XfD6q1800zH7LL8/vqf3n3b8s7s+OTt+ebS8MLk9trn999yzz6C1FSE1ViC1VV30UV70kuD1VVkyix30UaD1VZtzThmyy550Uh9003I7LT4/fV+00+J117d89H2/PPu+ef1+/Ho9+Cj4IGp4ol60klwzjzY8sry++50z0FszTa05pjs+eXp9+Hy++3Q77+J1133/PSi4IDm9tx00EHp+OCA1FF80030+/Dd89CM2GL5/fbM7biv45H9/v3B6qqg337R78BrzTSV22/l9tv4/PXy+u3M7rmo4Yil4ISy5ZWv5JHM7rp50ki66KFwzz120ET6/fiL12BqzTTZ8sv+//35/ffE669tzTeW23C355zV8cWy5Zaa3Xa96aVpzDOd3XnL7bj4/fax5ZWR2WiY3HK3553///625pvX8chuzjms4o2P2We4557X8cne9NGv5JL3/PXn997m9t3D6qyF1lnd9NFwzzz8/vzl9tzA6qmB1FSf3nyn4Yf9/vyR2mj6/fm05ZiS2mppzDK756J/01Cq4oqz5Zf1/PGZ3HOk4ILf9NNszTfk9tvv+ul00EK555/v+ejJ7bXp+OHq+OJrzTVkyit10EOo4oiq4ovs+eaN2GOc3nfW8cdzz0Dv+emH1lvs+OWg332+6ab2/PLV8cbK7bjV8cdxzz2s446T22u15pvN7rvu+eh20USG1lqB1FPb882B1FK+6afx+usAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABABAyZwAGAwgTKlzIsKHDhxAjSpxIsaJFiRjCzBEiEACtARdDihxJsqRJil1oAXgC8qTLlzBjuuzyJJTMmzhz6kwYquXOn0CDVjwotKhRo0SPKl3KtKnTp1CjSp1KtarVnNHevFH0JszVr0pDdXwiMBDYs0AJAQh1B+EQFQAIoZ2Ls8UThk/m0N0LcwEViXfuDOjSpS3CO10aCk6KuMsAw3ypqhACueGAFiu5AOAi18AbAJUNYLD7R3SgJ6hRz6ETeSqElW+SLuTyhOgdzYnvCGmxcAAAvZ7XJlTbQnZrp2GoCMn7BsJCQj4NbADwRvQc0ApDCTl4B4CKhdOjH/93imGIXYEqjCuMBsCsAbXuET7hLT0uQ+HjqRLauEHhnWiEBPgIAI8ghMF8RH3W0hxPPEIIgAGyB1x+VGGW0BtkUbGAXwD0h5B2LXGxAFFwbWiiiTZRyNQQ6qmF0GcTGhAGgQo9YZZaHhogllcqTgWABAwNiNACxlT2WY4GTGZAIAAkxd4ZPU7VAmVJHbjAkE84ZyBmSM74SF4LGUOFbAcOEaVSQyzgnVYSCGFMHggRstsbhLyxAJcKjUYFdgoNYYwxDhIiVnFnKoXBHMZ0NIdsEOwJm5cLDaoYgwI9QYh6hWaq6aacdurpp1GyBmqmdMQ3apSniXfqeHSQ1YKoq44Md9lYbMUa2R2nCRQQADs="
        load_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////+/v/z9vu9zeptkdFYgspMeMdEcsRYgcp7m9W6y+ne5vR4mdRHdMV5mtXb4/Pv8/qEo9hvktKwxOZJdsa1x+d0ltNTfslchMxjis5Vf8nJ1u7+//+SrdzR3PD7/P6pvuSMqNvH1O2Nqdv4+v2huOHG1O2Trd2RrNz6+/2nvONdhcxzldN6m9V+ntZSfMhGc8Viic53mNR8nNZ1l9Rbg8tPesd+ndZfhs1Fc8SIpdqDodjM2O/u8vrt8vrp7vju8vm5yulxlNJPe8jV3/Ls8Pnn7ffx9fvy9ftSfcmzxefo7vjt8vnr8Pnr8PjR3fGHpdnO2u9JdsXq7/nx9PqXsN5qj9Bmi89ojc9rj9DK1+/9/f7Y4vJyldLs8flli860xuf3+fzZ4vP5+v3I1e5njM+8zOrh6PZuktFehcygt+G4yelTfcl+ntdLd8b9/v/F0+1QfMiuwuZIdcWTrt39/v6etuBag8tvk9HB0OtNecfj6vb2+PyKptrm7PdRfMjZ4/N7nNW8zep1l9OxxOZylNLn7fhJdcbP2vDf5/Xq7/hHdcWUrt2GpNmtweW3yOiDotjc5PTd5fSEotjT3vH8/f7p7/jU3vHn7PeHpNna4/NRe8jY4fNQe8hUfsng6PbI1e2sweVagstvktH3+f3L2O9ehsxkis5Zgcve5vV8ndZXgMqetuH5+/1Vf8pLeMZli8/c5fTO2e9OecemvOPV3/GqwOTk6/dFcsRGc8Rjic6Xsd6Zsd/l6/fw9PqYsN+2yOj19/zY4vPb5PSpveTL1+5mjc/o7fff5vSzxueVr93K1+6BoNe7y+m+zuqctOBGdMXH1e3E0uyast+Srd2Ysd6qv+TE0+z09vtqjtB1ltPU3/Jiic1ojs8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABCDQjoQAFCgcQKkzIcKHDhhAfSoxIcaLFihgvaszIcaPCAg7MCBR4y8rBAyhTqlzJsqXLlzBjypxJs6ZNmw4iASDl4KbPn0CDCh1q8xSACSeJKl3KtKnSCYOcSp1KtWpKCpsQWt3KtStNrV7DihWbdKzZs2jTql3LluamApvaRgEQoq1dlg8AqGgrsq7dsnL1BvZ7t/BcO3zpFl58OAfbuYQXB94bs4CVQQ4ym2RJoQDmzIPicj71eVCBA33vAn4MADFMB1FI9Zjdg5SZU45RUgjxoPZsUlFOraRghvbsKCEgS747l3LLHCFqVzlF/dTcBVZQ5jg1e1B1FaQerP+MHcX7KStmFvRQvDyw65bce2zKndIOADMUHFvp4SCH/xwULMDeAcTcl99/FKggUAj0tZdWcy7lUEVrYKW0yQKkZHdAgxvmIJIZugnIoEo5WCGiaoy15lKApAzCYUIiWfFiShPch5IVACzAoX9zVeEga86RGGAPUa3k34QuaheCChNEYUYUAoKYwyA5uqTcj2odtuICTsjY0g0AJHnKA6QA4EQUD0ThhI0HhBCeS33NiKVXELIEIJlFkuhhmP7lFUWDCoJ4wCCkLGDlgGxVGJiPzykYmXYFONEDbpvcV4B/KYnUDEoFzHbpShcCwOicZ9Vp5JQ9PCCaSvaZMV+lZtC7l0MBeW2K0lyxkmgfoqSKpWWECj6AW0oKLuBiDpv04ESSg/YGgK0HFABAD1XkJqETa47Y61hzYeutt9UiC56ZD+SVI4P/KTjtA5JGMRe0s66Zo3pH9YhiYSqIEIW++j5Z3n8lNtOMk2aEq51/gzTTbxWbVCHCo5uo8KQIzbhYRRSjbtsWpv+l5JicJEYIssYkl+zTaSanLNQpxCiq8sszKSgczDTLdEqZkeRZ884qjTlSD67yzHMB6gIQEAA7"
        quit_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////+9/f6zs7xf3/sUFDsTk7rRUXwcXH2rKz+8/P//v796OjxfHz85eX98fHvbGztWlr2sLDvaWnsS0vvcHD4w8P0lZXuZWX3tLT71dX85OT97Oz84+P5ycnwd3frSEjygYH2qKjsUVH0mJj++Pj71tb61dX739///f35zc3rRkbrSkryiIjzkZHuX1/4u7v+9fX60ND72Njxfn7weHj729vweXntVFT3tbX+9vb1pKTsUlLygoL84eH5w8P+8fH1oqL719f+9PTuYmLtXFzvb2/va2vuXV3tV1fvbW30nZ3wcnLuYGDrSUnuZGT96envZmb3trbyhITsSkr4vr7//Pz+8vL1paX6zc397u7/+/v96ur84OD0mZnsT0/4wMD0nJz97+/tVVX5xsb2q6vxfX385ubwdHT1o6Pxe3vvaGjzkJD96+v5x8f85+f1np7vZ2f98PD0np75y8v2r6/0l5f97e3vamr3uLj++fn4wsL1oaH3sLD2p6fwbW372dn1p6fsTEzyi4vyjIz3t7f0mpr++vr3ubntWFj4xMT3s7PrR0fuYWHwenrwe3v6z8/72tr5yMj84uL2ra3yhYX2rq7yior73Nz5ysr0n5/zk5P0lpbzlJT609PzjY3uXl74vLz86en1n5/tU1Pwb2/uZmbyg4P2qanxeXn1qantW1sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABCLyESoyBgwgTKlzIsKHDhxAjSpxIsWJEMaXICBSYxYPFjyBDihxJciKqLACylCrJsqXLly3FZCEDs6bNmzgRklmZs6fPnxR5Ah1KtKjRo0iTKl3KtKnTp1CjlsLCIqrVkRkvXcqS5RIWjx89zLxK1mIXlFmweL0kEIvBsnBtskhZNaGYF12Fgix1CWzcuB4AXNKL8O5YkSz6/o1ruIvDqQB4lir1NiHlgxgNYtTYxYOHyouhlsr78AUAsKZpWgagWixND1jQau0COnTT0S8gnn1hEAsAx5YPe7hEU4wHvGQ817bNtBSA3A9ZzOz9W6Hz1ocNnPXLXHQW6A6l8+Q2kNp6dQPDVWs/3d3qaCy6vx/0DRzh9YOuEW5vH1Xm4IeHsEceAKlYJ1wW9XUhIH9OicHZY1vxlMp5CM0FXHr6dcSgd1nUtVCACQJwiF2xQSdWgQftt+FTgSFonW8pgJbSalmgKFaIHq7YlFhceaUWSocQFuAlqaTi21Y21ojQcGmlUp+OSolxyI+CUdVQKlpdkgJtVhowVY5dqEXkclAiJUYqHZapZnRZHELmmmqWckibLLBAGJxllpICVwi+iaeX/JXiQZ13/nlQRoYaelahiW4oVkqMNtodXxtNJymDYpwlUEAAOw=="

        title = [
            [sg.Text("Financial Use ONLY", font=("Helvetica", 25), size=(20, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Client information:", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.InputCombo(values=[], size=(19, 1), key="_FA_CLIENT_CB_"),
             sg.Button("", font=("Helvetica", 8), size=(4, 1), button_color=("black", "light gray"), key="_FA_NEW_BTN_",
                       border_width=0, image_data=new_client_ioc, tooltip="Add a new client")],
            [sg.Text("Invoice No.:", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.InputText(key="_FA_INV_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("S/C No.:", size=(15, 1), background_color="white", text_color="black", justification="center"),
             sg.InputText(key="_FA_SC_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("Date and Time:", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.InputText(key="_FA_DATE_IP_", size=(21, 1), enable_events=True),
             sg.CalendarButton('', font=("Helvetica", 8), size=(5, 1), target=(3, 1), key="_FA_DATE_PICKER_",
                               border_width=0, image_data=calendar_ico, tooltip="Choose a date")]
        ]

        column2 = [
            [sg.Text("Destination port: ", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.InputText(key="_FA_DES_PORT_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("Goods Description:", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.InputText(key="_FA_GOODS_DES_IP_", size=(25, 1), enable_events=True)],
            [sg.Text("Unit Price/AUD:", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.Spin(values=[i for i in range(1, 10000)], size=(23, 1), initial_value='1000', key="_FA_PRICE_SP_")],
            [sg.Text("Quantity/TON:", size=(15, 1), background_color="white", text_color="black",
                     justification="center"),
             sg.Spin(values=[i for i in range(1, 1000)], size=(23, 1), initial_value='20', key="_FA_QUA_SP_")]
        ]

        buttons = [
            [sg.Button("", size=(20, 1), button_color=("black", "light gray"), key="_FA_SAVE_BTN_",
                       image_data=save_btn_ioc, border_width=0, tooltip="Save Now"),
             sg.Button("", size=(20, 1), button_color=("black", "light gray"), key="_FA_LOAD_BTN_",
                       image_data=load_btn_ioc, border_width=0, tooltip="Load file"),
             sg.Button("", size=(20, 1), button_color=("black", "light gray"), key="_FA_CLA_BTN_",
                       image_data=clear_btn_ioc, border_width=0, tooltip="Clear All"),
             sg.Button("", size=(20, 1), button_color=("black", "light gray"), key="_FA_QUIT_BTN_",
                       image_data=quit_btn_ioc, border_width=0, tooltip="Quit the program")
             ]
        ]

        column_all = [
            [sg.Column(title, pad=(10, 10), background_color="white", key="_FA_TITL_COLUMN_", justification="center")],
            [sg.Column(column1, pad=(20, 10), background_color="white", key="_FA_COLUMN_1_"),
             sg.Column(column2, pad=(20, 10), background_color="white", key="_FA_COLUMN_2_")],
            [sg.Column(buttons, pad=(10, 30), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(10, 10), background_color="white")]
        ]

    def get_need_validate_fields(self) -> map:
        return {
            "_FA_INV_IP_": "[^0-9A-Za-z]",
            "_FA_SC_IP_": "[^0-9A-Za-z]",
            "_FA_DATE_IP_": "[^0-9 -:]",
            "_FA_PRICE_SP_": "[^0-9.]",
            "_FA_QUA_SP_": "[^0-9.]"
        }
