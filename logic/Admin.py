from logic.AbstractPackingInvoice import AbstractPackingInvoiceClass
from logic.Financial import Financial
from logic.Packing import Packing
from utils.Utils import update_client_list, load_exist_record, update_admin_table, disable_unnecessary_buttons


class Admin(AbstractPackingInvoiceClass):

    def run(self, main):
        field_data = {
            "_FA_CLIENT_CB_": "Client Name",
            "_FA_INV_IP_": "Invoice No.",
            "_FA_SC_IP_": "S/C No.",
            "_FA_DATE_IP_": "Date",
            "_FA_DES_PORT_IP_": "Destination port",
            "_FA_GOODS_DES_IP_": "Goods description",
            "_FA_PRICE_SP_": "Unit price",
            "_FA_QUA_SP_": "Quantity",
            "_PL_CLIENT_CB_": "Client Name",
            "_PL_INV_IP_": "Invoice No.",
            "_PL_SC_IP_": "S/C No.",
            "_PL_DATE_IP_": "Date",
            "_PL_DES_PORT_IP_": "Destination port",
            "_PL_GOODS_DES_IP_": "Goods description",
            "_PL_PACK_SP_": "Bags",
            "_PL_NET_SP_": "Net weight",
            "_PL_GROSS_SP_": "Gross weight",
            "_PL_CBM_SP_": "Total Measurement"
        }

        if self.event == "_AD_OPEN_BTN_":
            # TODO complete open the record by excel(generate the excel file)
            return True
        elif self.event == "_AD_EDIT_BTN_":
            # opening a window that can modify the record
            record = self.get_selected_record(main)
            # if record is false means there is no record selected
            if not record:
                return True
            if self.values["_AD_PKL_RAD_"]:
                packing = main.create_window("packing", "IPLMS - Packing List Generator",
                                             main.packing_ui.get_layout())
                disable_unnecessary_buttons(main.windows_map["packing"], ["_PL_LOAD_BTN_"])
                update_client_list(main, packing, "_PL_CLIENT_CB_")
                load_exist_record(main, "packing", field_data, record)
                packing.un_hide()

                flag = True
                while flag:
                    event3, values3 = packing.read()
                    print(event3, values3)
                    packing_logic = Packing(main, event3, values3, record)
                    flag = packing_logic.run(main)
                    record = flag
            elif self.values["_AD_INV_RAD_"]:
                financial = main.create_window("financial", "IPLMS - Invoice Generator",
                                               main.financial_ui.get_layout())
                disable_unnecessary_buttons(main.windows_map["financial"], ["_FA_LOAD_BTN_"])
                update_client_list(main, financial, "_FA_CLIENT_CB_")
                load_exist_record(main, "financial", field_data, record)
                financial.un_hide()

                flag = True
                while flag:
                    event3, values3 = financial.read()
                    print(event3, values3)
                    financial_logic = Financial(main, event3, values3, record)
                    flag = financial_logic.run(main)
                    record = flag
            update_admin_table(main, main.pck_inv_data_obj.data_map)
            return True
        elif self.event == "_AD_DEL_BTN_":
            # delete a selected record
            record = self.get_selected_record(main)
            self.remove_record(record)
            main.pck_inv_data_obj.save_data()
            update_admin_table(main, main.pck_inv_data_obj.data_map)
            # TODO show message box
            return True
        elif self.event == "_AD_SEARCH_BTN_":
            # the search
            condition = self.values["_AD_SCB_IPC_"]
            key_word = self.values["_AD_KEY_IP_"]
            result = self.search_record(condition, key_word)
            update_admin_table(main, result)
            return True
        elif self.event == "_AD_UGM_BTN_":
            # user_manage = main.create_window("user_manage", "IPLMS",
            #                                  main.user_manage_ui.get_layout(),
            #                                  disable_close=True)
            # user_manage.un_hide()
            # event, values = user_manage.read()
            # user_manage_logic = UserManage(main, event, values)
            # user_manage_logic.run(main)
            # user_manage.hide()
            return True
        elif self.event == "_AD_QUIT_BTN_" or self.event is None:
            # TODO show message box
            # TODO ask for saving the unsaved changes
            return False
        else:
            return True

    def get_selected_record(self, main):
        try:
            info = main.windows_map["admin"]['_AD_RET_TABLE_'].get()[self.values["_AD_RET_TABLE_"][0]]
        except IndexError:
            # TODO show message box (Please select a record)
            return False
        record = {}
        for each in self.data_map:
            if each["Invoice No."] == info[0]:
                record = each
                break
        return record

    def search_record(self, condition, key):
        result = []
        order = "ASC"
        if "(" in condition:
            order = condition.split("(")[1].replace(")", "")
            condition = condition.split("(")[0]
        for each in self.data_map:
            if key in str(each[condition]):
                result.append(each)
        if order == "DESC":
            return sorted(result, key=lambda res: res[condition], reverse=True)
        else:
            return sorted(result, key=lambda res: res[condition])
