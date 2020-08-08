from abc import abstractmethod, ABCMeta

import PySimpleGUI as sg

# import ui
from PySimpleGUI import Window

from beans.AbstractDataMap import DataMap
from beans.ClientData import ClientData
from beans.PackingInvoiceData import PackingInvoiceData
from beans.UserData import UserData
from ui.LoginUI import Login_UI
from ui.FinancialUI import Financial_UI
from ui.MessageBoxUI import MessageBox_UI
from ui.OpenRecordUI import OpenRecord_UI
from ui.PackingUI import Packing_UI
from ui.AdminUI import Admin_UI
from ui.ClientPageUI import Client_UI
from ui.NewUserPageUI import NewUser_UI
from ui.UserManagePageUI import UserMange_UI

from concurrent.futures import ThreadPoolExecutor


def init_data(data_type: DataMap) -> DataMap:
    data_type.init_data()
    try:
        data_obj = data_type.data_map
    except FileNotFoundError:
        data_type.init_file()
        data_obj = data_type.data_map
    return data_obj


class MainApplication(metaclass=ABCMeta):
    # init data
    user_data_obj = UserData()
    client_data_obj = ClientData()
    pck_inv_data_obj = PackingInvoiceData()

    data_pre = [user_data_obj, client_data_obj, pck_inv_data_obj]

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
        print(each)
        print(data[each])

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

    def create_window(self, window_id: str, window_name: str, layout: list, size=(0, 0), disable_close=False,
                      reload=False) -> Window:
        if window_id not in self.windows_map.keys() or reload:
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
        open_record_ui = OpenRecord_UI(row, col, data_list, header_list)
        window = sg.Window("Choose the record", open_record_ui.get_layout(), auto_size_buttons=False,
                           background_color="white", finalize=True, disable_close=True)
        return window

    @abstractmethod
    def on_enable(self):
        pass

    @abstractmethod
    def on_disable(self):
        pass
