from marathon import Marathon

class Participant:
    def __init__(self, id):
        self.id = id
        self.marathons = []
        self.total_marathons = 0
        self.failed_times = 0

    def __repr__(self):
        return "Participant {}\n".format(self.id)

    def add_marathon(self, date, name, type, time_finished, category):
        marathon = Marathon(date, name, type, time_finished, category)
        self.marathons.append(marathon)

    def json(self):
        return {
            'name': self.id,
            'marathons': [
                marathon.json() for marathon in self.marathons
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        participant = Participant(json_data['id'])
        marathons = []
        for marathon_data in json_data['marathons']:
            marathons.append(Marathon.from_json(marathon_data))
        participant.marathons = marathons

        return participant