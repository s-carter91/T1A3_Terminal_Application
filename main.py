# import time
import datetime
import pytz
from simple_term_menu import TerminalMenu
# import myfunctions
# import myclass

# person_list = []

class Person:
    def __init__(self, name, time_zone):
        self.name = name
        self.time_zone = time_zone
    
def countries():
    options = ["America", "Australia", "Europe"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    if options[menu_entry_index] == 'Australia':
        australia()
    elif options[menu_entry_index] == 'Europe':
        europe()
    else:
        print('Nope')
def australia():
    options = [i for i in pytz.all_timezones if i.startswith('Australia')]
    terminal_menu = TerminalMenu(options)
    aus_menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[aus_menu_entry_index]}!")
    person_time_zone = options[aus_menu_entry_index]
    return person_time_zone


# australia(person_time_zone='')

# print()
# print(aus_menu_entry_index)
# datetime.datetime.isoformat('04:23:01')
# print(zoneinfo.available_timezones())
# person1 = Person(name = input('please type persons name '), time_zone = (input('please type persons local ')))
# person1.time_zone = datetime.datetime.now(zoneinfo.ZoneInfo(person1.time_zone))

format = '%d-%m-%Y %H:%M'

america_countries = [i for i in pytz.all_timezones if i.startswith('Europe')]
print(america_countries)

person1 = Person(name = input('please type persons name '), time_zone = countries())
person1.time_zone = datetime.datetime.now(tz=pytz.timezone(person1.time_zone))

person2 = Person(name = 'Jeff', time_zone = input('please input time zone: '))
person2.time_zone = datetime.datetime.now(tz=pytz.timezone(person2.time_zone))

# for k, v in zoneinfo.available_timezones():
#     print(f' the value of {k} is {v}')

print(f'{person2.name} - {person2.time_zone.strftime(format)}')
