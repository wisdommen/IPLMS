from abc import abstractmethod, ABCMeta

import PySimpleGUI as sg

# import ui
from beans.cilentData import ClientData
from beans.packingInvoiceData import PackingInvoiceData
from beans.userData import UserData
from ui.LoginUI import Login, MessageBox
from ui.FinancialUI import Financial
from ui.PackingUI import Packing
from ui.AdminUI import Admin
from ui.ClientPageUI import Client
from ui.NewUserPageUI import NewUser
from ui.UserManagePageUI import UserMange


def init_data(data_type_list):
    data = {}
    for data_type in data_type_list:
        try:
            data_obj = data_type.data_map
        except FileNotFoundError:
            data_type.init_file()
            data_obj = data_type.data_map
        data[data_type] = data_obj
    return data


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

    data = init_data([user_data_obj, client_data_obj, pck_inv_data_obj])

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

    @abstractmethod
    def on_enable(self):
        pass

    @abstractmethod
    def on_disable(self):
        pass
