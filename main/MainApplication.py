from abc import abstractmethod, ABCMeta

import PySimpleGUI as sg

# import ui
from beans.cilentData import ClientData
from beans.packingInvoiceData import PackingInvoiceData
from beans.userData import UserData
from ui.LoginUI import Login, MessageBox
from ui.FinancialUI import Financial
from ui.OpenRecordUI import OpenRecord
from ui.PackingUI import Packing
from ui.AdminUI import Admin
from ui.ClientPageUI import Client
from ui.NewUserPageUI import NewUser
from ui.UserManagePageUI import UserMange

from concurrent.futures import ThreadPoolExecutor


def init_data(data_type):
    data_type.init_data()
    try:
        data_obj = data_type.data_map
    except FileNotFoundError:
        data_type.init_file()
        data_obj = data_type.data_map
    return data_obj


class MainApplication(metaclass=ABCMeta):
    # instantiate UI objects
    login_ui = Login()
    financial_ui = Financial()
    packing_ui = Packing()
    admin_ui = Admin()
    client_ui = Client()
    new_user_ui = NewUser()
    user_manage_ui = UserMange()
    mg = MessageBox()

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

    windows_map = {}

    def create_window(self, id, name, layout, size=(0, 0), disable_close=False):
        if id not in self.windows_map.keys():
            if size == (0, 0):
                window = sg.Window(name, layout, auto_size_buttons=False, background_color="white", finalize=True,
                                   disable_close=disable_close)
            else:
                window = sg.Window(name, layout, auto_size_buttons=False, background_color="white", finalize=True,
                                   disable_close=disable_close, size=size)
            self.windows_map[id] = window
            return window
        return self.windows_map[id]

    @staticmethod
    def create_open_record_window(row, col, data_list, header_list):
        open_record_ui = OpenRecord(row, col, data_list, header_list)
        window = sg.Window("Choose the record", open_record_ui.get_layout(), auto_size_buttons=False, background_color="white", finalize=True,
                           disable_close=True)
        return window

    @abstractmethod
    def on_enable(self):
        pass

    @abstractmethod
    def on_disable(self):
        pass
