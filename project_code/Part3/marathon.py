
class Marathon:
    def __init__(self, date, name, type, time_finished, category):
        self.date = date
        self.name = name
        self.type = type
        self.time_finished = time_finished
        self.category = category

    def __repr__(self):
        return "Marathon Date: {},\n Marathon Name: {},\n Marathon Type: {},\n Marathon Time: {},\n " \
               "Marathon Category: {}\n".format(self.date, self.name, self.type, self.time_finished, self.category)

    def json(self):
        return {
            'date': self.date,
            'name': self.name,
            'type': self.type,
            'time_finished': self.time_finished,
            'category': self.category
        }

    @classmethod
    def from_json(cls, json_data):
        return Marathon(**json_data)