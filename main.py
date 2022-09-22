import time
import datetime
import pytz
from simple_term_menu import TerminalMenu
import csv
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
    
    # def __str__(self):
    #     return f'Name = {self.name}, time_zone = {self.time_zone}'

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
    menu_entry_index = terminal_menu.show()
    person_time_zone = options[menu_entry_index]
    return person_time_zone
def america():
    options = [i for i in pytz.all_timezones if i.startswith('America')]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    person_time_zone = options[menu_entry_index]
    return person_time_zone
def europe():
    options = [i for i in pytz.all_timezones if i.startswith('Europe')]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    person_time_zone = options[menu_entry_index]
    return person_time_zone

def convert_time(timez):
    return datetime.datetime.now(tz=pytz.timezone(timez)).strftime(forma)

forma = '%d-%m-%Y %H:%M'

def option1():
    add_another_person = True
    while add_another_person != 'No':
        Person(name = input('Please type persons name: '), time_zone = countries())
        print('Would you like to add another person? \n')
        options = ['Yes', 'No']
        terminal_menu = TerminalMenu(options)
        add_menu_entry_index = terminal_menu.show()
        add_another_person = options[add_menu_entry_index]

# option1()

# Option 3:

def option3():
    with open('person_timezone.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(Person.person_name)
        writer.writerow(Person.person_time)
        # for i in range(len(Person.person_name)):
        #     row = Person.person_name[i], Person.person_time[i]
        #     writer.writerow(row)
    f.close()

# export_csv()
def import_csv():
    with open('person_timezone.csv', 'r') as f:
        csv_reader = csv.reader(f)
        imported_data =list(csv_reader)
        Person.person_name=imported_data[0]
        Person.person_time=imported_data[1]
    f.close()

# option1()
# with open('person_timezone.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     Person.person_time=list(csv_reader)[1]
# f.close()

# with open('person_timezone.csv', 'r') as f:
#   # read the file as a dictionary for each row ({header : value})
#     reader = csv.DictReader(f)
#     data = {}
#     for row in reader:
#         for header, value in row.items():
#             try:
#                 data[header].append(value)
#             except KeyError:
#                 data[header] = [value]

# # extract the variables you want
#     name = data['Person.person_name']
#     location = data['Person.person_time']

# Printing/Call function
def option2():
    person_country = Person.person_time.copy()
    person_time = [convert_time(i) for i in Person.person_time]
    person_name = [i for i in Person.person_name]
    for i in range(len(person_name)):
        print(f'{person_name[i]} : {person_country[i]} : {person_time[i]}')



# for item in Person.person_time:
#     datetime.datetime.now(tz=pytz.timezone(item)).strftime(forma)




# res = "\n".join("{} : {} : {}".format(x, y, z) for x, y, z in zip(person_name, person_country, person_time))
# print(res)
# print_name_zones = {person_name[i] : person_time[i] for i in range(len(person_name))}
# for x in print_name_zones.keys():
#     print(f'{x} : {print_name_zones[x]}')


# Exporting user list and timezone information to csv



# if person_time == False:
#     person_time = []
#     return person_time
# else:
#     print("Can't import a file after adding users.\nPlease restart the application and import before adding users")

# print(person_time)
# print(person_name)

    # for i in range(len(Person.person_name)):
    #     f.write("{} {}\n".format(Person.person_name[i], Person.person_time[i]))

print('Welcome to the TimeZo')
print('Do you have a file to import?')
print('(If this is your first time using the applcation select no)')
options = ['Yes', 'No']
terminal_menu = TerminalMenu(options)
start_menu_entry_index = terminal_menu.show()
if start_menu_entry_index == 0:
    import_csv()
else:
    print('No file imported, taking you to the main menu')

print('Welcome to the Main Menu')
print('Please select what you would like to do')
options = ['Add People to your List', 'View current times for all people added to your list', 'Export List', 'Close Application']
terminal_menu = TerminalMenu(options)
main_menu_entry_index = terminal_menu.show()
while main_menu_entry_index != 3:
    if main_menu_entry_index == 0:
        option1()
    elif main_menu_entry_index == 1:
        option2()
    elif main_menu_entry_index == 2:
        option3()
    print('Main Menu')
    options = ['Add People to your List', 'View current times for all people added to your list', 'Export List', 'Close Application']
    terminal_menu = TerminalMenu(options)
    main_menu_entry_index = terminal_menu.show()
        

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
# print_name_zones = {Person.person_name[i] : Person.person_time[i] for i in range(len(Person.person_name))}
# for x in print_name_zones.keys():
#     print(f'{x} : {print_name_zones[x]}')
# print(print_name_zones)

# print(Person.time_zone)