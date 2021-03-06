#!/usr/bin/python

from icalendar import Calendar, Event
from pytz import timezone
from datetime import date, datetime, timedelta
import sys

with open(sys.argv[1]) as f:
    ics_str = f.read(-1)

winnipeg = timezone('America/Winnipeg')

c = Calendar.from_ical(ics_str)

def next_seven_day_events(c):
    today = date.today()
    seven_from_today = today + timedelta(days=7)
    for e in c.walk():
        if isinstance(e, Event):
            event_daytime = e[u'DTSTART'].dt
            event_date = event_daytime
            time_str = ""
            if isinstance(e[u'DTSTART'].dt, datetime):
                event_daytime = event_daytime.astimezone(winnipeg)
                event_date = event_daytime.date()
                time_str = "%02d:%02d" % (
                    event_daytime.hour, event_daytime.minute)

            if today <= event_date <= seven_from_today:
                yield (event_date, time_str, e)
            

upcoming = list(next_seven_day_events(c))
upcoming.sort()

today = date.today()
for (event_date, time_str, e) in upcoming:
    print 'this {green}week at {red}Skullspace {yellow}' + \
    ("{green}today{yellow}" if event_date == today
     else event_date.strftime("%A") ) + \
    " -- {yellow}" +  e[u'SUMMARY'].encode('UTF8') + " {green}" + time_str


