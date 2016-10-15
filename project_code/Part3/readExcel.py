import csv
from participant import Participant

def open_file(path):

    reader = csv.reader(open(path, 'r'), delimiter=',', dialect='excel')
    participants = []
    participant = None
    rownum = 0
    for row in reader:
        participant_id = None
        marathon_date = None
        marathon_name = None
        marathon_type = None
        marathon_time = None
        marathon_category = None
        #participant.append(row)
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                if header[colnum] == "PARTICIPANT ID":
                    participant_id = col
                    participant = Participant(col)
                elif header[colnum] == "EVENT DATE":
                    marathon_date = col
                elif header[colnum] == "EVENT NAME":
                    marathon_name = col
                elif header[colnum] == "EVENT TYPE":
                    marathon_type = col
                elif header[colnum] == "TIME":
                    marathon_time = col
                    if marathon_time == "-1":
                        participant.failed_times += 1
                elif header[colnum] == "CATEGORY":
                    marathon_category = col
                    participant.total_marathons += 1
                    participant.add_marathon(marathon_date, marathon_name, marathon_type, marathon_time,
                                             marathon_category)
                else:
                    print("Exception!")

                colnum += 1

        participants.append(participant)

        rownum += 1

    return participants




path = 'Project1_data.csv'
participants = open_file(path)
id_number = 188

'''
print("The participant id\n", participants[id_number].id)
print("The participant participates {} times, and failed {} times with history\n {}"
      .format(participants[id_number].total_marathons,
              participants[id_number].failed_times,
              participants[id_number].marathons))
id_number = 8711
print("The participant id\n", participants[id_number].id)
print("The participant participates {} times, and failed {} times with history\n {}"
      .format(participants[id_number].total_marathons,
              participants[id_number].failed_times,
              participants[id_number].marathons))
              '''