# import time
import datetime
import zoneinfo
import pytz
# import myfunctions
# import myclass

# person_list = []

class Person:
    def __init__(self, name, time_zone = ' '):
        self.name = name
        self.time_zone = time_zone
# datetime.datetime.isoformat('04:23:01')
# print(zoneinfo.available_timezones())
# person1 = Person(name = input('please type persons name '), time_zone = (input('please type persons local ')))
# person1.time_zone = datetime.datetime.now(zoneinfo.ZoneInfo(person1.time_zone))

format = '%Y-%m-%d %H:%M'

person2 = Person(name = 'Sam', time_zone = 'America/Panama')
person2time = datetime.datetime.now(tz=pytz.UTC)



print(f'{person2.name} - {person2time.strftime(format)}')
