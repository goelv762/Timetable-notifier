import datetime

def parse_lines():
    TIMETABLE = open("./data/timetable.ics", "r")
    ALLOWED_PREFIX = ["DTSTART;", "SUMMARY:", "LOCATION:", "DESCRIPTION:"]

    raw_timetable_lines = TIMETABLE.readlines()
    new_timetable_lines = []

    for x in range(len(raw_timetable_lines)):
        if (raw_timetable_lines[x].startswith(tuple(ALLOWED_PREFIX))):
            new_timetable_lines.append(raw_timetable_lines[x])

    for y in range(len(new_timetable_lines)):
        for z in range(len(ALLOWED_PREFIX)):
            new_timetable_lines[y] = new_timetable_lines[y].replace(ALLOWED_PREFIX[z], "")
        
        colon_index = new_timetable_lines[y].find(':')
        if (colon_index != -1):
            new_timetable_lines[y] = new_timetable_lines[y][new_timetable_lines[y].find(':') + 1:]
            new_timetable_lines[y] = new_timetable_lines[y].replace("T", "")

    
    temp = open("./data/timetable.txt", "w")
    temp.writelines(new_timetable_lines)


parse_lines()

timetable = open("./data/timetable.txt", "r")
timetable_lines = timetable.readlines()
timetable.close()

for x in range(len(timetable_lines)):

    #gets current time and changes it so it can be compared to timetable time
    now = str(datetime.datetime.now())
    now = now.replace("-", "").replace(" ", "").replace(":", "")[: 12] + "00"
    now = int(now)

    try:
        if (int(timetable_lines[x]) < now):
            print(timetable_lines[x])
        
    except ValueError:
        pass
print(now)