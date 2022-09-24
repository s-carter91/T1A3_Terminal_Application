from datetime import datetime
import csv
import pytz
from simple_term_menu import TerminalMenu


class Person:
    '''Creates a person instance then stores name
    and time zone values to people list
    '''
    people = []
    def __init__(self, name, time_zone):
        self.name = name
        self.time_zone = time_zone
        Person.people.append(self)

    @staticmethod
    def find_person():
        '''Returns index of an element withing the Person.people list.
        Allows printing of a specific index in the list
        '''
        options = map(str, Person.people)
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        return Person.people[menu_entry_index]

    @staticmethod
    def get_all_person():
        '''Returns Person.people list to allow for printing'''
        return Person.people

    def my_name(self):
        '''used to retun name of Person.people elements'''
        return(self.name)

    def my_time(self):
        '''used to retun time zone of Person.people elements'''
        return(self.time_zone)

    def __str__(self):
        return (f'{self.name}, {self.time_zone}')


def countries():
    '''Returns  users options of countries to pick from
    to add as the timezone for instances created from
    the Person class.
    '''
    options = ['America', 'Australia', 'Europe']
    terminal_menu = TerminalMenu(options)
    country_menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[country_menu_entry_index]}")
    return cities(options[country_menu_entry_index])


def cities(name):
    '''Lists cities from pytz list that start with name parameter as options.'''
    options = [i for i in pytz.all_timezones if i.startswith(name)]
    terminal_menu = TerminalMenu(options)
    cities_menu_entry_index = terminal_menu.show()
    return options[cities_menu_entry_index]


def convert_time(timez):
    '''Converts pytz recognised timezone to a formatted date and time string.'''
    date_time_format = '%d-%m-%Y %H:%M'
    return datetime.now(tz=pytz.timezone(timez)).strftime(date_time_format)


def import_csv():
    '''imports data from csv with name person_timezone.csv
    and creates a Person instance with imported data
    '''
    with open('person_timezone.csv', 'r') as f:
        csv_reader = csv.reader(f)
        imported_data =list(csv_reader)
        for each_line in imported_data:
            Person(each_line[0], each_line[1])
            f.close()


def option1():
    '''Calls the person class to create a user.'''
    add_another_person = True
    while add_another_person != 'No':
        Person(name = input('Please type persons name: '), time_zone = countries())
        print('Would you like to add another person? \n')
        options = ['Yes', 'No']
        terminal_menu = TerminalMenu(options)
        add_menu_entry_index = terminal_menu.show()
        add_another_person = options[add_menu_entry_index]


def selection_2():
    '''Loop menu to execute based on return of selection_menu_2'''
    option2_menu_entry_index = selection_2_menu()
    while option2_menu_entry_index != 2:
        if option2_menu_entry_index == 0:
            selection_2_call_individual()
        elif option2_menu_entry_index == 1:
            option_2_call_all()
        options = ["View Individuals Time", "View All Peoples Times", 'Return to Main Menu']
        terminal_menu = TerminalMenu(options)
        option2_menu_entry_index = terminal_menu.show()


def selection_2_menu():
    '''Returns users selection of how to view Person.people list'''
    options = ['View Individuals Time', 'View All Peoples Times', 'Return to Main Menu']
    terminal_menu = TerminalMenu(options)
    option2_menu_entry_index = terminal_menu.show()
    return option2_menu_entry_index


def selection_2_call_individual():
    '''Prints name and formatted time zone of element returned
    from find_person
    '''
    x = Person.find_person()
    print(x.my_name(), convert_time(x.my_time()))


def option_2_call_all():
    '''Prints all elements names and converted timezones 
    returned from get_all_person
    '''
    for i in Person.get_all_person():
        print(f'{i.my_name()} - {convert_time(i.my_time())}')


def option3():
    '''Exports Person.people list csv named person_timezone.csv'''
    with open('person_timezone.csv', 'w') as f:
        writer = csv.writer(f)
        for i in Person.get_all_person():
            writer.writerow([i.name, i.time_zone])
        print('\nYour list of people has now been exported.'
' Next time you run the application, you may import this file.\n')
        f.close()

option1()
option2()
