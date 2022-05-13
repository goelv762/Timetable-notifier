def parse_lines():
    TIMETABLE = open("./data/timetable.ics", "r")
    ALLOWED_PREFIX = ["DTSTART", "DTEND", "SUMMARY", "LOCATION"]

    raw_timetable_lines = TIMETABLE.readlines()
    new_timetable_lines = []

    for x in range(len(raw_timetable_lines)):
        if (raw_timetable_lines[x].startswith(tuple(ALLOWED_PREFIX))):
            new_timetable_lines.append(raw_timetable_lines[x])

    
parse_lines()