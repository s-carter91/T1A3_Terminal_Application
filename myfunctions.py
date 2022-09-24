from datetime import datetime
import csv
import pytz
from simple_term_menu import TerminalMenu


class Person:
    people = []
    def __init__(self, name, time_zone):
        self.name = name
        self.time_zone = time_zone
        Person.people.append(self)

    @staticmethod
    def find_person():
        options = map(str, Person.people)
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        return Person.people[menu_entry_index]

    @staticmethod
    def get_all_person():
        return Person.people

    def my_name(self):
        return(self.name)

    def my_time(self):
        return(self.time_zone)

    def __str__(self):
        return (f'{self.name}, {self.time_zone}')

    # def __repr__(self):
    #     return (f'{self.my_name()} : {self.my_time()}')

def countries():
    options = ['America', 'Australia', 'Europe']
    terminal_menu = TerminalMenu(options)
    country_menu_entry_index = terminal_menu.show()
    # print(f"You have selected {options[menu_entry_index]}!")
    if options[country_menu_entry_index] == 'Australia':
        return australia()
    elif options[country_menu_entry_index] == 'Europe':
        return europe()
    elif options[country_menu_entry_index] == 'America':
        return america()
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
    return options[menu_entry_index]

def convert_time(timez):
    date_time_format = '%d-%m-%Y %H:%M'
    return datetime.now(tz=pytz.timezone(timez)).strftime(date_time_format)

def import_csv():
    with open('person_timezone.csv', 'r') as f:
        csv_reader = csv.reader(f)
        imported_data =list(csv_reader)
        for each_line in imported_data:
            Person(each_line[0], each_line[1])
            f.close()

def selection_2_menu():
    options = ['View Individuals Time', 'View All Peoples Times', 'Return to Main Menu']
    terminal_menu = TerminalMenu(options)
    option2_menu_entry_index = terminal_menu.show()
    return option2_menu_entry_index
# Feature 1 uses the function below:
def option1():
    add_another_person = True
    while add_another_person != 'No':
        Person(name = input('Please type persons name: '), time_zone = countries())
        print('Would you like to add another person? \n')
        options = ['Yes', 'No']
        terminal_menu = TerminalMenu(options)
        add_menu_entry_index = terminal_menu.show()
        add_another_person = options[add_menu_entry_index]


# Feature 3 uses the function below:
def option3():
    with open('person_timezone.csv', 'w') as f:
        writer = csv.writer(f)
        for i in Person.get_all_person():
            writer.writerow([i.name, i.time_zone])
        print('''\nYour List of people has now been exported.
 Next time you run the application, you may import this file.\n''')
        f.close()

# y = Person.get_all_person()
# print(y.mytime())
# y = Person.get_all_person()
# y.mytime.convert_time

        # options = map(str, Person.people)
        # terminal_menu = TerminalMenu(options)
        # menu_entry_index = terminal_menu.show()
        # return Person.people[menu_entry_index]

def option2():
    option2_menu_entry_index = selection_2_menu()
    while option2_menu_entry_index != 2:
        if option2_menu_entry_index == 0:
            option_2_call_individual()
        elif option2_menu_entry_index == 1:
            option_2_call_all()
        options = ["View Individuals Time", "View All Peoples Times", 'Return to Main Menu']
        terminal_menu = TerminalMenu(options)
        option2_menu_entry_index = terminal_menu.show()    


def option_2_call_individual():
    x = Person.find_person()
    print(x.my_name(), convert_time(x.my_time()))

def option_2_call_all():
    for i in Person.get_all_person():
        print(f'{i.my_name()} - {convert_time(i.my_time())}')
option1()
option2()
# print(Person..my_name(), convert_time(Person.people.my_time()))
# convert_time (Person.get_all_person.my_time())
# print(Person.get_all_person())
# print(Person.people.index)
# print(Person.find_people())
# Person.find_people
# Person.my_name
# print(Person.my_time)
# print(Person.people)
# add_another_person = True
# while add_another_person != 'No':
#     count = 0
#     count += 1
#     Person(name = input('Please type persons name: '), time_zone = countries())
#     store_people = []
#     store_people.append(f'{Person.person_dict} {count}')
#     print('Would you like to add another person? \n')
#     options = ['Yes', 'No']
#     terminal_menu = TerminalMenu(options)
#     add_menu_entry_index = terminal_menu.show()
#     add_another_person = options[add_menu_entry_index]
    