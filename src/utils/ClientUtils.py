from src.logic.Client import Client
from src.main.MainApplication import MainApplication
from src.utils.Utils import getUUID
from utils.logger import log


def create_new_client(main: MainApplication) -> str:
    """ This method will create a window for entering or loading client information into a window

    Args:
        main: MainApplication class which is the abstract main body of the program

    Returns: A string of the client name

    """
    client = main.create_window("client", "IPLMS", main.client_ui.get_layout(), disable_close=True)
    client["_CLIENT_ID_"].Update(getUUID())
    client["_CP_NAME_IP_"].Update("")
    client["_CP_PHONE_IP_"].Update("")
    client["_CP_ADDRESS_IP_"].Update("")
    client.un_hide()
    event4, values4 = client.read()
    log(event4 + " " + values4)
    client_logic = Client(main, event4, values4)
    name = client_logic.run(main)
    client.hide()
    return name

