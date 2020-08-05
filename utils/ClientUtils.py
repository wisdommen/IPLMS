from logic.Client import Client
from utils.Utils import getUUID


def create_new_client(main):
    client = main.create_window("client", "IPLMS", main.client_ui.get_layout(), disable_close=True)
    client["_CLIENT_ID_"].Update(getUUID())
    client["_CP_NAME_IP_"].Update("")
    client["_CP_PHONE_IP_"].Update("")
    client["_CP_ADDRESS_IP_"].Update("")
    client.un_hide()
    event4, values4 = client.read()
    print(event4, values4)
    client_logic = Client(main, event4, values4)
    client_logic.run(main)
    client.hide()

