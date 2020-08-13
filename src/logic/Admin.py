from src.logic.AbstractPackingInvoice import AbstractPackingInvoiceClass
from src.logic.Financial import Financial
from src.logic.Packing import Packing
from src.main.MainApplication import MainApplication
from src.utils.Utils import update_client_list, load_exist_record, update_admin_table, disable_unnecessary_buttons


class Admin(AbstractPackingInvoiceClass):

    # Overriding method
    def run(self, main: MainApplication) -> bool:
        # documentation see abstract class

        # The field_data formed by the window elements' key as key and the corresponding header of the data_map as
        # values
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
        elif self.event == "_AD_EDIT_PL_BTN_" or self.event == "_AD_EDIT_IN_BTN_":
            # get the record that been selected to edit
            record = self.get_selected_record(main)
            # if record is false means there is no record selected
            if not record:
                # do nothing because there is no record selected, just finish this loop :)
                return True
            if self.event == "_AD_EDIT_PL_BTN_":
                # create or get the window object
                packing = main.create_window("packing", "IPLMS - Packing List Data Entry Form",
                                             main.packing_ui.get_layout())
                # disable the unnecessary button when the window open by admins
                disable_unnecessary_buttons(main.windows_map["packing"], ["_PL_LOAD_BTN_"])
                # update the client list in the drop-down list of the window
                update_client_list(main, packing, "_PL_CLIENT_CB_")
                # load the select into the edit window
                load_exist_record(main, "packing", field_data, record)
                packing.un_hide()

                # Start the loop of the edit window until close the edit window, then the forces will be
                # back to admin window
                flag = True
                while flag:
                    event3, values3 = packing.read()
                    print(event3, values3)
                    # use iteration to loop again until while loop ended
                    packing_logic = Packing(main, event3, values3)
                    # get if it is going to have next loop
                    flag = packing_logic.run(main)
            elif self.event == "_AD_EDIT_IN_BTN_":
                # create or get the window object
                financial = main.create_window("financial", "IPLMS - Invoice Data Entry Form",
                                               main.financial_ui.get_layout())
                # disable the unnecessary button when the window open by admins
                disable_unnecessary_buttons(main.windows_map["financial"], ["_FA_LOAD_BTN_"])
                # update the client list in the drop-down list of the window
                update_client_list(main, financial, "_FA_CLIENT_CB_")
                # load the select into the edit window
                load_exist_record(main, "financial", field_data, record)
                financial.un_hide()

                # Start the loop of the edit window until close the edit window, then the forces will be
                # back to admin window
                flag = True
                while flag:
                    event3, values3 = financial.read()
                    print(event3, values3)
                    # use iteration to loop again until while loop ended
                    financial_logic = Financial(main, event3, values3)
                    # get if it is going to have next loop
                    flag = financial_logic.run(main)
            # update the admin table even if there is no change
            update_admin_table(main, main.pck_inv_data_obj.data_map)
            return True
        elif self.event == "_AD_DEL_BTN_":
            # delete a selected record
            record = self.get_selected_record(main)
            if main.mg.show_ask_box("Are you sure to delete the record?") == "Yes":
                self.remove_record(record)
                main.pck_inv_data_obj.save_data()
                # update the change to the admin table
                update_admin_table(main, main.pck_inv_data_obj.data_map)
                # show message box
                main.mg.show_info_box("Record Deleted!")
            return True
        elif self.event == "_AD_SEARCH_BTN_":
            # the search (Filtering)
            # get the filter condition and the key words for filtering
            condition = self.values["_AD_SCB_IPC_"]
            key_word = self.values["_AD_KEY_IP_"]
            # do search
            result = self.search_record(main, condition, key_word)
            update_admin_table(main, result)
            return True
        elif self.event == "_AD_UGM_BTN_":
            # I am not going to implement this function due to the time constrain
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
            # show message box confirm quit
            # hide the main window to prevent user change anything when answering quit confirmation
            main.windows_map["admin"].hide()
            if main.mg.show_ask_box("Are you sure to quit?") == "Yes":
                return False
            main.windows_map["admin"].un_hide()
            return True
        else:
            return True

    def get_selected_record(self, main: MainApplication) -> map:
        """ This method returns a record map that selected in the table element

        Args:
            main: MainApplication class which is the abstract main body of the program

        Returns: a map that contains the packing list and invoice data of the selected record

        """
        try:
            # "main.windows_map["admin"]['_AD_RET_TABLE_'].get()" gets the all records from admin table elements
            # "[self.values["_AD_RET_TABLE_"][0]]" get the values that has been selected
            info = main.windows_map["admin"]['_AD_RET_TABLE_'].get()[self.values["_AD_RET_TABLE_"][0]]
        except IndexError:
            # show message box (Please select a record)
            main.mg.show_warning_box("Please select a record!")
            return False
        record = {}
        for each in self.data_map:
            if each["Invoice No."] == info[0]:
                record = each
                break
        return record

    def search_record(self, main: MainApplication, condition: str, key: str) -> list:
        """ This method implements the filter part, which return a list of sorted records which meets the condition

        Args:
            main: MainApplication class which is the abstract main body of the program
            condition: a string which gives the filter condition
            key: a string that should be contained in the result

        Returns: a list of sorted records which meets the condition

        """
        result = []
        order = "ASC"
        if condition == "":
            # show condition show not be empty
            main.mg.show_warning_box("Search condition should not be empty!")
            return self.data_map
        # get the sort order (Ascending or Descending)
        if "(" in condition:
            order = condition.split("(")[1].replace(")", "")
            condition = condition.split("(")[0]
        # filter the data records
        for each in self.data_map:
            if key in str(each[condition]):
                result.append(each)
        # sort the result
        if order == "DESC":
            return sorted(result, key=lambda res: res[condition], reverse=True)
        else:
            return sorted(result, key=lambda res: res[condition])
