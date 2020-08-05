from utils.ClientUtils import create_new_client
from utils.Utils import clear_all_input, load_record
from logic.AbstractPackingInvoice import AbstractPackingInvoiceClass


class Packing(AbstractPackingInvoiceClass):

    def run(self, main):
        field_data = {
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
        if self.event == "_PL_NEW_BTN_":
            create_new_client(main)
            return True
        elif self.event == "_PL_LOAD_BTN_":
            # opening a record select window and load a record to fields
            self.record = load_record(self, main, main.pck_inv_data_obj, "packing", field_data)
            return True
        elif self.event == "_PL_CLA_BTN_":
            clear_all_input(main.windows_map["packing"], self.values)
            return True
        elif self.event == "_PL_SAVE_BTN_":
            # save the record
            for each in self.values.values():
                if each != "":
                    self.save(main, field_data)
            return True
        elif self.event == "_PL_QUIT_BTN_" or self.event is None:
            # TODO ask for saving the unsaved changes
            return False
        else:
            return True
