class OpenRecord(object):
    def __init__(self, event, values):
        self.event = event
        self.values = values
        self.record = {}

    def run(self, main, fields):
        info = main.Element('_OR_TABLE_').get()[self.values["_OR_TABLE_"][0]]
        main.close()
        i = 0
        for each in fields:
            self.record[each] = info[i]
            i += 1
        return self.record


