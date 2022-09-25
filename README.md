# Timezoco 

### Error Handling

Sigted the menuProactive error handling by using the menus.

### R5 - Styling Guides

#### PEP-8 - Style Guide for Python Code

##### Imports
With library imports, I have imported specific methods from the library where possible  
Also listed in the correct order as per the documentation (1: Standard library imports 2: Related third party imports 3: Local application/library specific imports)

##### Maximum Line Length
No single line of code is longer than the 99 characters that PEP8 states as a maximum character per line limit (except if Docstring or Comment which have a maximum line length of 72 characters).

##### General PEP8 Formatting
Double blank lines have been added around top level functions and classes.

#### PEP-257 - Docstring Conventions

##### One-line and Multi-line Docstrings

Docstrings have been added to all functions and formatted correctly based on if they are single or multi-line as per PEP-257.


##### 

### Features

##### Feature 1 - Creating People Objects

The first feature of the application allows the end user to create and store a person within the application. When the user selects "add a new person" they will be asked to input a name and a timezone.

##### Feature 2 - Displaying Current Time of Stored People

The second feature allows the end user to display the current times of the people who were stored using the first or third feature. The user will have two options within this feature for how they want to display users. They can either select a person from a menu list they want to view the current time for or display all of the people objects that have been stored. 

##### Feature 3 - Import and Export of Stored People

The third feature provides a way for the user to import the stored list via a CSV file or export the current stored list to a CSV file. When the user runs the applcation, they will be asked if they want to import a file of people (advised to tick no if it's the first time running the app). Once 