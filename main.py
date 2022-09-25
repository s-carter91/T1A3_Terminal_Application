import time
import csv
from simple_term_menu import TerminalMenu
import myfunctions

# import myfunctions
# import myclass

# person_list = []




    
    # def __str__(self):
    #     return f'Name = {self.name}, time_zone = {self.time_zone}'

    # def update_time(self):
    #     Person.time_zone = 

    # @staticmethod
    # def list_display():
    #     return [
    #         Person.
    #     ]
    






# option1()

# Option 3:


# export_csv()


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

print('Welcome to the Time Zoco')
print('Do you have a file to import?')
print('(If this is your first time using the applcation select no)')
options = ['Yes', 'No']
terminal_menu = TerminalMenu(options)
start_menu_entry_index = terminal_menu.show()
if start_menu_entry_index == 0:
    myfunctions.import_csv()
else:
    print('No file imported, taking you to the main menu')

print('Welcome to the Main Menu')
print('Please select what you would like to do')
# options = [
#     'Add, edit or remove people',
#      'View current time for created people',
#      'Export list of people',
#      'Close application'
#      ]
# terminal_menu = TerminalMenu(options)
# main_menu_entry_index = terminal_menu.show()
# while main_menu_entry_index != 3:
#     if main_menu_entry_index == 0:
#         myfunctions.main_menu_option_1()
#     elif main_menu_entry_index == 1:
#         myfunctions.main_menu_option_2()
#     elif main_menu_entry_index == 2:
#         myfunctions.main_menu_option_3()
#     print('Main Menu')
#     options = ['Add People to your List', 'View current times for all people added to your list', 'Export List', 'Close Application']
#     terminal_menu = TerminalMenu(options)
#     main_menu_entry_index = terminal_menu.show()
        

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

