from abc import abstractmethod, ABCMeta

import PySimpleGUI as sg

# import ui
from PySimpleGUI import Window

from src.beans.AbstractDataMap import DataMap
from src.beans.ClientData import ClientData
from src.beans.PackingInvoiceData import PackingInvoiceData
from src.beans.UserData import UserData
from src.ui.LoginUI import Login_UI
from src.ui.FinancialUI import Financial_UI
from src.ui.MessageBoxUI import MessageBox_UI
from src.ui.OpenRecordUI import OpenRecord_UI
from src.ui.PackingUI import Packing_UI
from src.ui.AdminUI import Admin_UI
from src.ui.ClientPageUI import Client_UI
from src.ui.NewUserPageUI import NewUser_UI
from src.ui.UserManagePageUI import UserMange_UI

from concurrent.futures import ThreadPoolExecutor

from utils.logger import log


def init_data(data_type: DataMap) -> DataMap:
    """ This method invoke the initiation method in each data object to initiate data.

    Args:
        data_type: The data object

    Returns: initiated data object

    """
    data_type.init_data()
    try:
        data_obj = data_type.data_map
    except FileNotFoundError:
        data_type.init_file()
        data_obj = data_type.data_map
    return data_obj


class MainApplication(metaclass=ABCMeta):
    """This method is the abstract class for main entry.

        All main entries should inherit this class, so it can do data initiation and windows initiation before
    application starts.
    """

    # init data objects
    user_data_obj = UserData()
    client_data_obj = ClientData()
    pck_inv_data_obj = PackingInvoiceData()

    data_pre = [user_data_obj, client_data_obj, pck_inv_data_obj]

    # use thread pool to create threads to load data, save resources and loading time if is gave a huge amount of data
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = {}
        for each in data_pre:
            task = executor.submit(init_data, each)
            tasks[each] = task
        data = {}
        for each in tasks.keys():
            result = tasks[each].result()
            data[each] = result

    for each in data.keys():
        log(str(each))
        log(str(data[each]))

    # instantiate UI objects
    login_ui = Login_UI()
    financial_ui = Financial_UI()
    packing_ui = Packing_UI()
    admin_ui = Admin_UI()
    client_ui = Client_UI()
    new_user_ui = NewUser_UI()
    user_manage_ui = UserMange_UI()
    mg = MessageBox_UI()

    windows_map = {}

    def create_window(self, window_id: str, window_name: str, layout: list, size=(0, 0), disable_close=True) -> Window:
        """ This method creates a window if not exists and stores it into the windows map, or returns a window if
        already exists.

        Args:
            window_id: a string, the unique id of a window, it should not .
            window_name: a string, the window name which will appear in the title of the window.
            layout: a list, the window layout.
            size: a tuple, the size of the window, if not specific, the window will be auto-sized.
            disable_close: a boolean, if the window can not be closed by the cross on the title bar, if not specific,
                            the window will not disable close by the cross on the title bar.

        Returns: a window object

        """
        if window_id not in self.windows_map.keys():
            if size == (0, 0):
                window = sg.Window(window_name, layout, auto_size_buttons=False, background_color="white",
                                   finalize=True, disable_close=disable_close)
            else:
                window = sg.Window(window_name, layout, auto_size_buttons=False, background_color="white",
                                   finalize=True, disable_close=disable_close, size=size)
            self.windows_map[window_id] = window
            return window
        return self.windows_map[window_id]

    @staticmethod
    def create_open_record_window(row: int, col: int, data_list: list, header_list: list) -> Window:
        """ This method creates a load record window which should be destroyed after using

        Args:
            row: a int of how many rows will be in the table in the window
            col: a int of how many columns will be in the table in the window
            data_list: a list of all the data records should be displayed
            header_list: a lost of the header

        Returns: a window object

        """
        open_record_ui = OpenRecord_UI(row, col, data_list, header_list)
        window = sg.Window("Choose the record", open_record_ui.get_layout(), auto_size_buttons=False,
                           background_color="white", finalize=True, disable_close=True)
        return window

    @abstractmethod
    def on_enable(self):
        """ All logics of the application while running should write in this method.

        Returns: void

        """
        pass

    @abstractmethod
    def on_disable(self):
        """ All logics of the application while closing should write in this method.

        Returns: void

        """
        pass
