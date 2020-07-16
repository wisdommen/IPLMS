import PySimpleGUI as sg

"""
Summary: This class is the main body layout of the GUI
"""


class NewUser(object):
    # private element, shouldn't be changed from outside
    _layout = []

    # initiate the layout
    def __init__(self):
        save_btn_ioc = b"R0lGODlhoAAjAHAAACwAAAAAoAAjAIf////+//74+/bd7NOgyYWAtlxzr0twrUd8tFacxn/T5sb1+fLl8N6dx4Hn8eH1+vKaxX6bxn/L4bvA266GumSBtlyly4vP48LZ6s7i79rg7dfZ6c692aqFuWLM4r37/fn+/v7e7NTf7dbq8+T5/Pfu9emWw3h2sE/J4brV58l4sVGhyYbr9Obo8eGKvGjY6Mzp8+Kjyonu9ep4slGfyITC3LCDuGDb6tDE3bP3+/WZxHxyrkm11J+Bt12t0Ja11aCRwHKv0Ze01J+v0ZhyrkqUwXWu0Jaz052hyYeAtlufyIPw9uueyIOky4q01J6nzY5/tVqEuWH9/v3b69HO48DP5MGu0Zfk8N3L4b3W6Mrh7tjp8uOx0pt8tFfu9unL4bzR5cTs9ObA262s0JTJ4Ln0+fHP48Gt0JWZxHvm8d/N4r/Q5MLt9efQ5MOSwHKQv3Hn8eCDuF/+/v3k793K4bt3sU/x9+292al7s1V+tVmEuGG41qSjyojU5seGuWN9tFeCuF+616fy+O53sVDs9eeLvGnX6MyYxHqYxHvH37h0r0ySwXPi7trm8N/s9OfL4ryZxXzv9uvH37eiyYfw9+ynzY32+vPR5cOVwnfk79yLvGrp8uKJu2fW58qIu2aGumOy05us0JXz+O+ozY/t9ejo8uHm8N7j79zM4r6KvGmUwnXX6Mvv9urn8d/9/vy616b8/vvc69Gjy4nC3LGiyoeSwHOPvm6Pv2+TwXSgyYS41qO21aHz+fCsz5ONvmx4slLB3LDS5cV9tVi+2qz5+/f3+vSmzI3I4LnD3bJxrkjU5si82amHumSVwnbj79vl8N3I37nn8uCUwnb8/fvj8Nu516XO47/0+fCXw3qNvW3F3rW516Tp8+Pe7NWpzpGIumbK4Lu516b1+vO31qPV58iz1J3d7NS/2q2MvWq31qLh7tmky4txrklwrUiSwXK/2633+vWXw3kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI/wABCFTHpMKOAwgTKlzIsKHDhxAjSpxIsaJFiDsQHLImUGCLQxdDihxJsqRJiQcPtQBQDOTJlzBjynx5CIC1mThz6tyZcJknnkCDCrWIAMHQo0iTKl3KtKnTp1CjSp1KtarVqxQtgIulTl2sZRWwih0KbiDXlYLejF2bcwe4YrEOJjwko8VPnbFgsKXKRFBchkx87ozVYu/UZQBcQjzCBIEFwQjf+Ejnw4dahZKtUG6M8JAPGQA0K67AJJ1mC0YNA0UQS0ZqiABiXVAHjgnCz7S5yvCRmkkLQeBSqJOxzKgPcIKAW/PRmXDwWIKsXVat05O6FmEjAqBdVMUBH4J8qv9QgWCZINsHUgjyNL68IAsHMv4mf9AT4SIIxhcBTn1nkeuvPQSADHIhhJx3Ce0HDoIL9QUfQi0UlhB4ih2AQAoyoNffTP/ZJdF2ClknwxuelOhJEbHEcldRJvoAAHMIwSDhbQBYYGKJFggC44YzYRigQ7EpVIQMgrQw3HBGgvPTG9BF2AJoDx4Ag149AWCkk9fFoiGPMSG2JZDqYDZcESeS+AaZO7wRoQ9MnOjijjIqBJ4PnpBIJpk/cnnSkOoUmFBgqQWZkAoXCKKCn1VOd4AFxUQZ54QAMLEDonrOtANif/355F2CVglOiFoegJhinqTwYkKPItThXQeosAw4eVaCalJZ23GljpXTdZpQWeosc8QF2xVxgCcyyADOEcvUpWNCt6aQjo3fDQjOMsm+SKmsJjEBTlfqpFCcQupo05AP3PbK6hvberXMISlUKBxtdx2SLm1fYmvvvfjmq+++/Pbrb7+K/outJ58KfO+oBmO7n5UVJtyfSh0BF7DDa6EriEABAQA7"
        cancel_btn_ioc = b"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"

        title = [
            [sg.Text("Create a new user group", font=("Helvetica", 15), size=(20, 1), background_color="white",
                     text_color="red", justification="center")]
        ]

        column1 = [
            [sg.Text("Group Name:", font=("arial", 10), background_color="white", text_color="black"),sg.InputText(key="_NU_PHONE_IP_", size=(25, 1), enable_events=True)]
        ]

        column2 = [
            [sg.Text("Password: ",font=("arial", 10), background_color="white", text_color="black"),sg.InputText(key="_NU_NAME_IP_", size=(25, 1), enable_events=True)]
        ]

        buttons = [
            [sg.Button(image_data=save_btn_ioc,border_width=0, size=(20, 1), button_color=("black", "light gray"), key="_NU_CREATE_BTN_"),
            sg.Button(image_data=cancel_btn_ioc, border_width=0, size=(20, 1), button_color=("black", "light gray"),
                       key="_NU_CANCEL_BTN")]
        ]

        column_all = [
            [sg.Column(title, background_color="white", key="_NU_TITLE_COLUMN_",  justification="center")],
            [sg.Column(column1, background_color="white", key="_NU_NAME_COLUMN_",pad=(10,10), justification="center")],
            [sg.Column(column2, background_color="white", key="_NU_PASSWORD_COLUMN_",pad=(10,10), justification="center")],
            [sg.Column(buttons, pad=(10, 20), background_color="white", justification="center")],
        ]

        self._layout = [
            [sg.Column(column_all, pad=(20, 10), background_color="white", justification="center")]
        ]

    # outside method can get the layout by this method
    def get_layout(self):
        return self._layout