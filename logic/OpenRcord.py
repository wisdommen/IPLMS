class OpenRecord(object):
    def __init__(self, event, values):
        self.event = event
        self.values = values
        self.record = {}

    def run(self, main):
        info = main.Element('_OR_TABLE_').get()[self.values["_OR_TABLE_"][0]]
        main.close()
        self.record["Client ID"] = info[0]
        self.record["Client Name"] = info[1]
        self.record["Client Phone Number"] = info[2]
        self.record["Client Address"] = info[3]
        return self.record


