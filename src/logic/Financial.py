from src.main.MainApplication import MainApplication
from src.utils.ClientUtils import create_new_client
from src.utils.Utils import clear_all_input, load_record, update_client_list, validate_input
from src.logic.AbstractPackingInvoice import AbstractPackingInvoiceClass


class Financial(AbstractPackingInvoiceClass):

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
            "_FA_QUA_SP_": "Quantity"
        }

        if self.event == "_FA_NEW_BTN_":
            name = create_new_client(main)
            # chart the new client name into the field
            main.windows_map["financial"]["_FA_CLIENT_CB_"].Update(name)
            update_client_list(main, main.windows_map["financial"], "_FA_CLIENT_CB_")
            return True
        elif self.event == "_FA_LOAD_BTN_":
            # opening a record select window and load a record to fields
            return load_record(self, main, main.pck_inv_data_obj, "financial", field_data)
        elif self.event == "_FA_CLA_BTN_":
            # show message box
            if main.mg.show_ask_box("Are you sure to clear all inputs?") == "Yes":
                clear_all_input(main.windows_map["financial"], self.values)
            return True
        elif self.event == "_FA_SAVE_BTN_":
            # save the record
            print(self.record)
            for each in self.values.values():
                if each != "":
                    # check validation
                    result = validate_input(main.financial_ui, field_data, self.values)
                    if len(result) > 0:
                        string_builder = ""
                        for string in result:
                            string_builder = string_builder + string + "\n"
                        main.mg.show_warning_box(string_builder)
                        return True
                    self.save(main, field_data)
                    main.pck_inv_data_obj.save_data()
                    # show message box
                    main.mg.show_info_box("Record Saved!")
                    return True
            # show message box
            main.mg.show_warning_box("There is nothing to save!")
            return True
        elif self.event == "_FA_QUIT_BTN_":
            main.windows_map["financial"].hide()
            # ask for saving the unsaved changes
            if main.mg.show_ask_box("Are you sure to quit the edit window?") == "Yes":
                if main.mg.show_ask_box("Would you like to save?") == "Yes":
                    result = validate_input(main.financial_ui, field_data, self.values)
                    if len(result) > 0:
                        string_builder = ""
                        for string in result:
                            string_builder = string_builder + string + "\n"
                        main.mg.show_warning_box(string_builder)
                        main.windows_map["financial"].un_hide()
                        return True
                    self.save(main, field_data)
                    main.pck_inv_data_obj.save_data()
                    # show message box
                    main.mg.show_info_box("Record Saved!")
                return False
            main.windows_map["financial"].un_hide()
            return True
        elif self.event is None:
            return False
        else:
            return True
