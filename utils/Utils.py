import re
import time

from PySimpleGUI import Window

from beans.AbstractDataMap import DataMap
from logic import AbstractLogic
from logic.OpenRcord import OpenRecord
from ui.AbstractUI import UI


def getUUID() -> int:
    return int(time.time() * 1000)


def make_table(num_rows: int, num_cols: int, data_list: list) -> list:
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    for i in range(0, len(data_list)):
        data[i] = list(data_list[i].values())
    return data


def clear_all_input(window: Window, values: map) -> None:
    for each in values.keys():
        window[each].Update("")


def load_record(logic_class: AbstractLogic, main, data_obj: DataMap, window_id: str,
                field_data: map) -> map or bool:
    header = data_obj.header
    opened_records = main.create_open_record_window(len(logic_class.data_map), len(header), logic_class.data_map,
                                                    header)
    opened_records.un_hide()
    event, values = opened_records.read()
    print(event, values)
    open_record_logic = OpenRecord(event, values)
    try:
        record = open_record_logic.run(opened_records, header)
    except IndexError:
        values = {'_OR_TABLE_': [0]}
        open_record_logic = OpenRecord(event, values)
        record = open_record_logic.run(opened_records, header)
    if event != "_OR_CAN_BTN_":
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
    window = main.windows_map[window_id]
    keys = check_elements_exist(window, field_data)
    for each in keys:
        window[each].Update(record[field_data[each]])


def update_client_list(main, window: Window, field_name: str) -> None:
    clients = []
    for each in main.client_data_obj.data_map:
        clients.append(each["Client Name"])
    window[field_name].Update(values=clients)


def update_admin_table(main, data_list: list) -> None:
    header_list = ["Invoice No.", "Client Name", "Date", "Goods description"]
    data = [[j for j in range(4)] for i in range(len(data_list))]
    for i in range(0, len(data_list)):
        record = []
        for each in header_list:
            record.append(data_list[i][each])
        data[i] = record
    main.windows_map["admin"]["_AD_RET_TABLE_"].Update(values=data)


def check_elements_exist(window: Window, field_data: map) -> list:
    elements = []
    for element in window.element_list():
        if element.Key in field_data.keys():
            elements.append(element.Key)
    return elements


def disable_unnecessary_buttons(window: Window, keys: list) -> None:
    for each in keys:
        window[each].Update(disabled=True)


def validate_input(window_ui: UI, field_map: map, values: map) -> list:
    results = []
    fields = window_ui.get_need_validate_fields()
    for each in fields.keys():
        input_value = str(values[each])
        if input_value == "":
            results.append("In %s: Empty input" % field_map[each])
            continue
        validate_rule = fields[each]
        result = re.search(validate_rule, input_value)
        if result is not None:
            result = result.span()
        else:
            continue
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
