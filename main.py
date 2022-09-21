import time
import datetime
import pytz
from simple_term_menu import TerminalMenu
# import myfunctions
# import myclass

# person_list = []

class Person:
    person_name = []
    person_time = []
    def __init__(self, name, time_zone):
        Person.person_name.append(name)
        Person.person_time.append(time_zone)
        self.name = name
        self.time_zone = time_zone
    
    def __str__(self):
        return f'Name = {self.name}, time_zone = {self.time_zone}'

    # def update_time(self):
    #     Person.time_zone = 

    # @staticmethod
    # def list_display():
    #     return [
    #         Person.
    #     ]
    
def countries():
    options = ["America", "Australia", "Europe"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    # print(f"You have selected {options[menu_entry_index]}!")
    if options[menu_entry_index] == 'Australia':
        return australia()
    elif options[menu_entry_index] == 'Europe':
        return europe()
    elif options[menu_entry_index] == 'America':
        return america()
    else:
        print('Nope')
def australia():
    options = [i for i in pytz.all_timezones if i.startswith('Australia')]
    terminal_menu = TerminalMenu(options)
    aus_menu_entry_index = terminal_menu.show()
    person_time_zone = options[aus_menu_entry_index]
    return datetime.datetime.now(tz=pytz.timezone(person_time_zone)).strftime(format)
def america():
    options = [i for i in pytz.all_timezones if i.startswith('America')]
    terminal_menu = TerminalMenu(options)
    aus_menu_entry_index = terminal_menu.show()
    person_time_zone = options[aus_menu_entry_index]
    return datetime.datetime.now(tz=pytz.timezone(person_time_zone)).strftime(format)
def europe():
    options = [i for i in pytz.all_timezones if i.startswith('Europe')]
    terminal_menu = TerminalMenu(options)
    aus_menu_entry_index = terminal_menu.show()
    person_time_zone = options[aus_menu_entry_index]
    return datetime.datetime.now(tz=pytz.timezone(person_time_zone)).strftime(format)

format = '%d-%m-%Y %H:%M'
# def option1():

add_another_person = 'Yes'
while add_another_person == 'Yes':
    Person(name = input('Please type persons name: '), time_zone = countries())
    print('Would you like to add another person? \n')
    options = ['Yes', 'No']
    terminal_menu = TerminalMenu(options)
    add_menu_entry_index = terminal_menu.show()
    add_another_person = options[add_menu_entry_index]
    
def option2():
    print_name_zones = {Person.person_name[i] : Person.person_time[i] for i in range(len(Person.person_name))}
    for x in print_name_zones.keys():
        print(f'{x} : {print_name_zones[x]}')





# main_menu_entry_index = ' '
# while main_menu_entry_index != 'Close Application':
#     print('Welcome to the Main Menu')
#     print('Please select what you would like to do')
#     options = ['Add People to your List', 'View current times for all people added to your list', 'Import List', 'Export List', 'Close Application']
#     terminal_menu = TerminalMenu(options)
#     main_menu_entry_index = terminal_menu.show()
#     add_another_person = 'Yes'
#     if options[main_menu_entry_index] == 'Add People to your List':
#         while add_another_person == 'Yes':
#             option1()

# def countries():
#     options = ["America", "Australia", "Europe"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     # print(f"You have selected {options[menu_entry_index]}!")
#     return options[menu_entry_index]

# def cities():
#     options = [i for i in pytz.all_timezones if i.startswith(countries())]
#     terminal_menu = TerminalMenu(options)
#     aus_menu_entry_index = terminal_menu.show()
#     # print(f"You have selected {options[aus_menu_entry_index]}!")
#     person_time_zone = options[aus_menu_entry_index]
#     return datetime.datetime.now(tz=pytz.timezone(person_time_zone)).strftime(format)

# australia(person_time_zone='')

# print()
# print(aus_menu_entry_index)
# datetime.datetime.isoformat('04:23:01')
# print(zoneinfo.available_timezones())
# person1 = Person(name = input('please type persons name '), time_zone = (input('please type persons local ')))
# person1.time_zone = datetime.datetime.now(zoneinfo.ZoneInfo(person1.time_zone))


# person_list = ()
# america_countries = [i for i in pytz.all_timezones if i.startswith('Europe')]
# print(america_countries)

# Person(name = input('name '), time_zone = (datetime.datetime.now(tz=pytz.timezone(countries()))))

# person1 = Person(name = input('please type persons name '), time_zone = countries())
# person1.time_zone = datetime.datetime.now(tz=pytz.timezone(person1.time_zone))
# person_list = {person1.name: person1.time_zone.strftime(format)}

# person_list[0:20].time_zone = datetime.datetime.now(tz=pytz.timezone(Person.time_zone)
# person2 = Person(name = 'Jeff', time_zone = countries())

# person2.time_zone = datetime.datetime.now(tz=pytz.timezone(person2.time_zone))

# for k, v in zoneinfo.available_timezones():
#     print(f' the value of {k} is {v}')
# Person.person_time = datetime.datetime.now(tz=pytz.timezone(Person.person_time))



# Person.person_dict.values() = datetime.datetime.now(tz=pytz.timezone(Person.person_dict.values()))

# print(f'{person1.name} - {person1.time_zone.strftime(format)}')
# print_name_zones = {[Person.person_name]: Person.person_time}

# print(f'{Person.person_name[0]} : {Person.person_time[0]}')
# for key, value in print_name_zones.items():
#     print("{} : {}".format(key, value))
# def option2():
print_name_zones = {Person.person_name[i] : Person.person_time[i] for i in range(len(Person.person_name))}
for x in print_name_zones.keys():
    print(f'{x} : {print_name_zones[x]}')
# print(print_name_zones)

# print(Person.time_zone)