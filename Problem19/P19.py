import datetime
from datetime import timedelta

day = datetime.datetime(1901, 1, 1)
counter = 0
while day.timetuple()[0] < 2001:
    if day.timetuple()[2] == 1 and day.timetuple()[6] == 6:
        counter += 1
    day += timedelta(days=1)
print(counter)