class Book():
    def __init__(self, call_num, title):
        self.call_num = call_num
        self.title = title

class Record(Book):
    def __init__(self, acc_num, call_num, title, new, discard, condition, status):
        super().__init__(call_num, title)
        self.acc_num = acc_num
        self.new = new
        self.discard = discard
        self.condition = condition
        self.status = status

class Data:
    def __init__(self):
        self.all_records = {}
    def addRecord(self, record):
        if record.acc_num in self.all_records.keys():
            print(">> Book copy has already been recorded.")
        else:
            info = [record.call_num, record.title, record.new,
                    record.discard, record.condition, record.status]
            return record.acc_num, info