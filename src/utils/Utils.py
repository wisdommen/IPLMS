import re
import time

from PySimpleGUI import Window

from src.beans.AbstractDataMap import DataMap
from src.logic import AbstractLogic
from src.logic.OpenRcord import OpenRecord
from src.ui.AbstractUI import UI


def getUUID() -> int:
    """ This method generates a uuid.

    Returns: a int that is a uuid for this program.

    """
    return int(time.time() * 1000)


def make_table(num_rows: int, num_cols: int, data_list: list) -> list:
    """ This method returns a list that uses for creating a table element.

    Args:
        num_rows: a int of how many rows.
        num_cols: a int of how many columns.
        data_list: a list that contains maps of records data.

    Returns: a list that uses for creating a table element.

    """
    # generates the frame of the table
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    # fill the frame with data
    for i in range(0, len(data_list)):
        data[i] = list(data_list[i].values())
    return data


def clear_all_input(window: Window, values: map) -> None:
    """ This method cleans given inputs of input fields in a window

    Args:
        window: a window that needs to be clean.
        values: the field that needs to be clean.

    Returns: void

    """
    for each in values.keys():
        window[each].Update("")


def load_record(logic_class: AbstractLogic, main, data_obj: DataMap, window_id: str,
                field_data: map) -> map or bool:
    """ This method controls the logic of open record window, returns a map of the record that can be used to fill the
    fields in the window or a boolean if user did a delete operation.

    Args:
        logic_class: a logic class which inherits from AbstractLogic class.
        main: MainApplication class which is the abstract main body of the program.
        data_obj: a data object which inherits from DataMap class.
        window_id: a string of the unique window id.
        field_data: a map contains all fields in the window and matched header in the data map.

    Returns: a map of the record that can be used to fill the fields in the window or a boolean if user did a delete
                operation.

    """
    header = data_obj.header
    # create the open record window
    opened_records = main.create_open_record_window(len(logic_class.data_map), len(header), logic_class.data_map,
                                                    header)
    opened_records.un_hide()
    event, values = opened_records.read()
    print(event, values)
    # create open record logic
    open_record_logic = OpenRecord(event, values)
    try:
        record = open_record_logic.run(opened_records, header)
    except IndexError:
        values = {'_OR_TABLE_': [0]}
        open_record_logic = OpenRecord(event, values)
        record = open_record_logic.run(opened_records, header)
    if event != "_OR_CAN_BTN_":
        # ask confirm if user want to delete a record
        if event == "_OR_DEL_BTN_" and main.mg.show_ask_box("Are you sure to delete the record?") == "Yes":
            # ask for confirm
            logic_class.remove_record(record)
            data_obj.save_data()
            # show message box
            main.mg.show_info_box("Record Deleted!")
            load_record(logic_class, main, data_obj, window_id, field_data)
            return True
        load_exist_record(main, window_id, field_data, record)
    return record


def load_exist_record(main, window_id: str, field_data: map, record: map) -> None:
    """ This method load a provided record to a window.

    Args:
        main: MainApplication class which is the abstract main body of the program.
        window_id: a string of the unique window id.
        field_data: a map contains all fields in the window and matched header in the data map.
        record: a map which is a data record.

    Returns: void.

    """
    window = main.windows_map[window_id]
    keys = check_elements_exist(window, field_data)
    for each in keys:
        window[each].Update(record[field_data[each]])


def update_client_list(main, window: Window, field_name: str) -> None:
    """ This method update the drop-down list of clients field in a window.

    Args:
        main: MainApplication class which is the abstract main body of the program.
        window: a window which needs to be update.
        field_name: a string of the field name of the window that needs to be updated.

    Returns: void.

    """
    clients = []
    for each in main.client_data_obj.data_map:
        clients.append(each["Client Name"])
    window[field_name].Update(values=clients)


def update_admin_table(main, data_list: list) -> None:
    """ This method updates the table in the admin window.

    Args:
        main: MainApplication class which is the abstract main body of the program.
        data_list: a list that contains maps of records data.

    Returns: void.

    """
    header_list = ["Invoice No.", "Client Name", "Date", "Goods description"]
    data = [[j for j in range(4)] for i in range(len(data_list))]
    for i in range(0, len(data_list)):
        record = []
        for each in header_list:
            record.append(data_list[i][each])
        data[i] = record
    main.windows_map["admin"]["_AD_RET_TABLE_"].Update(values=data)


def check_elements_exist(window: Window, field_data: map) -> list:
    """ This method check if the elements exists in a window and returns a list that contains the exists elements.

    Args:
        window: a window that need to check.
        field_data: a map contains all fields in the window and matched header in the data map.

    Returns: a list that contains the exists elements.

    """
    elements = []
    for element in window.element_list():
        if element.Key in field_data.keys():
            elements.append(element.Key)
    return elements


def disable_unnecessary_buttons(window: Window, keys: list) -> None:
    """ This method disables the specific button in the window.

    Args:
        window: a window that need to be operated.
        keys: a list of key of the button that need to be disabled.

    Returns: void

    """
    for each in keys:
        window[each].Update(disabled=True)


def validate_input(window_ui: UI, field_map: map, values: map) -> list:
    """ This method check validation of the input fields of a window.

    Args:
        window_ui: a UI object which inherits from UI class.
        field_map: a map contains all fields in the window and matched header in the data map.
        values: a map that contains the field keys and value inputs.

    Returns: a list of fields which are not valid with mark and tips.

    """
    results = []
    fields = window_ui.get_need_validate_fields()
    for each in fields.keys():
        input_value = str(values[each])
        if input_value == "":
            results.append("In %s: Empty input" % field_map[each])
            continue
        validate_rule = fields[each]
        # use regular expression to match the string if matched means not valid
        result = re.search(validate_rule, input_value)
        if result is not None:
            result = result.span()
        else:
            continue
        # mark where is not valid
        try:
            start = input_value[:result[0]]
        except IndexError:
            start = ""
        try:
            end = input_value[result[1]:]
        except IndexError:
            end = ""
        results.append("In %s: Invalid input marked inside the []\n   at \"%s[%s]%s\"" %
                       (field_map[each], start, input_value[result[0]:result[1]], end))
    return results
