from utils.ClientUtils import create_new_client
from utils.Utils import clear_all_input, load_record
from logic.AbstractPackingInvoice import AbstractPackingInvoiceClass


class Financial(AbstractPackingInvoiceClass):

    def run(self, main):
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
            create_new_client(main)
            return True
        elif self.event == "_FA_LOAD_BTN_":
            # opening a record select window and load a record to fields
            load_record(self, main, main.pck_inv_data_obj, "financial", field_data)
            return True
        elif self.event == "_FA_CLA_BTN_":
            clear_all_input(main.windows_map["financial"], self.values)
            return True
        elif self.event == "_FA_SAVE_BTN_":
            # save the record
            self.save(main, field_data)
            return True
        elif self.event == "_FA_QUIT_BTN_" or self.event is None:
            # TODO ask for saving the unsaved changes
            return False
        else:
            return True
