import time

from logic.OpenRcord import OpenRecord


def getUUID():
    return int(time.time() * 1000)


def make_table(num_rows, num_cols, data_list):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    for i in range(0, len(data_list)):
        data[i] = list(data_list[i].values())
    return data


def clear_all_input(window, values):
    for each in values.keys():
        window[each].Update("")


def load_record(logic_class, main, data_obj, window_id, field_data):
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
        if event == "_OR_DEL_BTN_":
            # TODO ask for confirm
            logic_class.remove_record(record)
            load_record(logic_class, main, data_obj, window_id, field_data)
            # TODO show message box
            return True
        window = main.windows_map[window_id]
        for each in field_data.keys():
            window[each].Update(record[field_data[each]])
    return record


def update_client_list(main, window, field_name):
    clients = []
    for each in main.client_data_obj.data_map:
        clients.append(each["Client Name"])
    window[field_name].Update(values=clients)
