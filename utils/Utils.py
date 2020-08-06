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
            logic_class.save(logic_class.data_map)
            load_record(logic_class, main, data_obj, window_id, field_data)
            # TODO show message box
            return True
        load_exist_record(main, window_id, field_data, record)
    return record


def load_exist_record(main, window_id, field_data, record):
    window = main.windows_map[window_id]
    keys = check_elements_exist(window, field_data)
    for each in keys:
        window[each].Update(record[field_data[each]])


def update_client_list(main, window, field_name):
    clients = []
    for each in main.client_data_obj.data_map:
        clients.append(each["Client Name"])
    window[field_name].Update(values=clients)


def update_admin_table(main, data_list):
    header_list = ["Invoice No.", "Client Name", "Date", "Goods description"]
    data = [[j for j in range(4)] for i in range(len(data_list))]
    for i in range(0, len(data_list)):
        record = []
        for each in header_list:
            record.append(data_list[i][each])
        data[i] = record
    main.windows_map["admin"]["_AD_RET_TABLE_"].Update(values=data)


def check_elements_exist(window, field_data):
    elements = []
    for element in window.element_list():
        if element.Key in field_data.keys():
            elements.append(element.Key)
    return elements
