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
        self.name = name.capitalize()
        self.time_zone = time_zone
        if name != None:
            Person.people.append(self)
        else:
            print('Please enter a name')
        # if name not in self.people:
        #     Person.people.append(self)
        # else:
        #     print('There is already a user with the same name. Try again by adding a last name')

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

    @staticmethod
    def get_person_del():
        '''Deletess instance of Person from Person.people list'''
        options = map(str, Person.people)
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        del Person.people[menu_entry_index]

    def __del__(self):
        del self
    
    def my_name(self):
        '''used to retun name of Person.people elements'''
        return(self.name)

    def my_time(self):
        '''used to retun time zone of Person.people elements'''
        return(self.time_zone)

    def __str__(self):
        return (f'{self.name}, {self.time_zone}')


class NoUsersToDisplay(Exception):
    pass

class IncorrectName(Exception):
    pass

class DuplicateName(IncorrectName):
    pass

class EmptyNameInput(IncorrectName):
    def __init__(self, username, message='Name field cannot be empty'):
        self.username = username
        self.message = message

    def check_name_empty1(self):
        if len(self) == 0:
            raise EmptyNameInput(self)
        return(self) 
        
    def __str__(self):
        return self.message


def startup():
    print('Welcome to the Time Zoco')
    print('Do you have a file to import?')
    print('(If this is your first time using the applcation select no)')
    options = ['Yes', 'No']
    terminal_menu = TerminalMenu(options)
    start_menu_entry_index = terminal_menu.show()
    if start_menu_entry_index == 0:
        import_csv()
        print(f'You have imported ')
    else:
        print('No file imported, taking you to the main menu')

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


def countries():
    '''Returns  users options of countries to pick from
    to add as the timezone for instances created from
    the Person class.
    '''
    print('Please select the Continent/Country/Area!')
    print('(If you would prefer to select from GMT, please select Etc from the menu)')
    options = [
        'America', 'Asia', 'Atlantic', 'Australia', 'Canada', 'Egypt', 'Europe', 'Japan',
         'NZ', 'Pacific', 'Poland', 'Portugal', 'Singapore', 'Turkey', 'US', 'Etc'
        ]
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


# def check_if_importing():
#     print('Welcome to the Time Zoco')
#     print('Do you have a file to import?')
#     print('(If this is your first time using the applcation select no)')
#     options = ['Yes', 'No']
#     terminal_menu = TerminalMenu(options)
#     start_menu_entry_index = terminal_menu.show()
#     if start_menu_entry_index == 0:
#         import_csv()
#     else:
#         print('No file imported, taking you to the main menu')


def main_menu_options():
    options = [
    'Add, edit or remove people',
     'View current time for created people',
     'Export list of people',
     'Close application'
     ]
    terminal_menu = TerminalMenu(options)
    main_menu_entry_index = terminal_menu.show()
    return main_menu_entry_index


def main_menu():
    print('Welcome to the Main Menu')
    print('Please select what you would like to do')
    main_menu_selection = main_menu_options()
    while main_menu_selection != 3:
        if main_menu_selection == 0:
            main_menu_option_1()
        elif main_menu_selection == 1:
            main_menu_option_2()
        elif main_menu_selection == 2:
            main_menu_option_3()
        print('Main Menu')
        main_menu_selection = main_menu_options()


def main_menu_option_1():
    '''Loop menu to execute based on return of selection_menu_2'''
    option2_menu_entry_index = person_list_update_choice()
    while option2_menu_entry_index != 3:
        if option2_menu_entry_index == 0:
            add_person()
        elif option2_menu_entry_index == 1:
            update_time_zone()
        elif option2_menu_entry_index == 2:
            remove_person()
        option2_menu_entry_index = person_list_update_choice()


def check_name_empty():
    '''Error handling for Empty Name field'''
    x = ''
    while x == '':
        try: 
            x = input('Please enter the persons name: ')
        except len(x) == 0:
            print('Persons name cannot be empty')
            raise EmptyNameInput('Name field cannot be empty')
        else:
            return x


# def check_name_empty():
#     '''Error handling for Empty Name field'''
#     x = ''
#     while x == '':
#         x = input('Please enter the persons name: ')
#         if len(x) == 0:
#             print('Persons name cannot be empty')
#         else:
#             return x


def check_name(self):
    # x = ' '
    # while x == ' ':
    z=[]
    for i in Person.get_all_person():
        z.append(i.my_name())
    if self in z:
        del self
        print('That person already exists, please try another name')
        return None
    else:
        return self
def add_person():
    '''Calls the person class to create a user.'''
    add_another_person = True
    while add_another_person != 'No':
        name_input = None
        while name_input == None:
            name_input = check_name_empty()
            print(name_input)
            name_input = check_name(name_input)
            print(name_input)
        Person(name = name_input, time_zone = countries())
        print('Would you like to add another person? \n')
        options = ['Yes', 'No']
        terminal_menu = TerminalMenu(options)
        add_menu_entry_index = terminal_menu.show()
        add_another_person = options[add_menu_entry_index]


def person_list_update_choice():
    '''Returns users selection of create/edit/delete to edit Person.people list'''
    options = ['Add new person', 'Edit persons time zone', 'Delete Person', 'Return to Main Menu']
    terminal_menu = TerminalMenu(options)
    option2_menu_entry_index = terminal_menu.show()
    return option2_menu_entry_index


def update_time_zone():
    '''Updates already stored persons time zone'''
    print('Please select the person you would like to update the time zone of?\n')
    x = Person.find_person()
    print(f'Please select the time zone that you want to move {x.name} to')
    x.time_zone = countries()
    print(f"{x.name}'s time zone has been update to {x.time_zone}") 
    return x.time_zone


def remove_person():
    '''Removes class instance of person'''
    print('Please select the person you would like to remove?\n')
    Person.get_person_del()


# print(pytz.all_timezones)
# def check_duplicate():
#     for i in Person.get_all_person()
#         if i.my_name 



def main_menu_option_2():
    '''Loop menu to execute based on return of selection_menu_2'''
    option2_menu_entry_index = display_choices()
    while option2_menu_entry_index != 2:
        if option2_menu_entry_index == 0:
            display_individual()
        elif option2_menu_entry_index == 1:
            display_all()
        option2_menu_entry_index = display_choices()


def display_choices():
    '''Returns users selection of how to view Person.people list'''
    options = ['View Individuals Time', 'View All Peoples Times', 'Return to Main Menu']
    terminal_menu = TerminalMenu(options)
    option2_menu_entry_index = terminal_menu.show()
    return option2_menu_entry_index


def display_individual():
    '''Prints name and formatted time zone of element returned
    from find_person
    '''
    print('Please select the person you would like to view the current time for')
    x = Person.find_person()
    print(f'{x.my_name()} - {x.my_time()} - {convert_time(x.my_time())}')


def display_all():
    '''Prints all elements names and converted timezones 
    returned from get_all_person
    '''
    for i in Person.get_all_person():
        print(f'{i.my_name()} - {i.my_time()} - {convert_time(i.my_time())}')


def main_menu_option_3():
    '''Exports Person.people list csv named person_timezone.csv'''
    with open('person_timezone.csv', 'w') as f:
        writer = csv.writer(f)
        for i in Person.get_all_person():
            writer.writerow([i.name, i.time_zone])
        print('\nYour list of people has now been exported.'
' Next time you run the application, you may import this file.\n')
        f.close()




startup()
main_menu()
# # remove_person()
# selection_2_call_individual()
# option_2_call_all()