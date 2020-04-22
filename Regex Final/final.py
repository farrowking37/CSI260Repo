"""Provides ability to search Windows Syslogs using various regex patterns.


Author: John Shultz
Class: CSI-260-03
Assignment: Regex Mini Final
Due Date: April 29th, 2020 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import csv
import re


class Logs(list):
    """Extends the builtin class of list to provide extra functionality"""

    def __init__(self):
        """Creates a standard list object.
        """
        super().__init__()

    def search(self, user_pattern):
        """Uses regex to search the logs object for matching logs.

        :param user_pattern: The desired regex pattern
        :return: A new Logs object containing all matching logs.
        """
        regex_pattern = re.compile(user_pattern)
        matching_logs = Logs()

        for line in self:
            if re.match(regex_pattern, line):
                matching_logs.append(line)

        return matching_logs


def match_handle(passed_logs, match_pattern):
    """Handles the process of getting matches from Log.search.
    To use, use statement like logs - match_handle(logs, pattern)
    :param passed_logs: (Logs) A Logs object to be searched through
    :param match_pattern: (String) The regex pattern to use in the match
    :return: Either passed_logs or matched_logs based on user input.
    """

    # Search for matches and save results to a new Logs
    matched_logs = passed_logs.search(match_pattern)

    # Notify user of how many new logs were found.
    print(f'We found {len(matched_logs)} logs!)')

    # Ask user if they want to print found results to screen
    print_check = str(input("Do you want to print them? (Y/N):"))

    # If they do, loop through all logs and print out a neat version of the log
    if print_check.lower() == "y":
        print(["Level", "Date", "Source", "EventID", "Category", "Desc."])
        for current_log in matched_logs:
            current_log = current_log.split(",")

            print(
                f'Level: {current_log[0]}\n'
                f'Date: {current_log[1]}\n'
                f'Source: {current_log[2]}\n'
                f'EventID: {current_log[3]}\n'
                f'Category: {current_log[4]}\n'
                f'Description: {current_log[5]}\n'
            )

    # Ask the user if they want to update the value of logs
    update_logs = str(input("Do you want to search these logs again (Y/N)?"))

    # If they do, return the value of matched_logs
    if update_logs.lower() == "y":
        return matched_logs

    # If they do not, return the originally passed logs.
    else:
        return passed_logs


# Open up the provided WindowsSyslogForPython.csv and read out all lines into
# A Logs object named all_logs
with open('WindowsSyslogForPython.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, dialect='excel')
    all_logs = Logs()
    for row in csv_reader:
        all_logs.append(','.join(row))

# Create a string to define our menu
menu_options = "\n1.) Print a list of all logs (for debugging).\n" \
            "2.) Search within log level\n" \
            "3.) Search for a specific date\n" \
            "4.) Search within log Source\n" \
            "5.) Search for a specific EventID\n" \
            "6.) Search within Task Category\n" \
            "7.) Search within Description\n" \
            "8.) Enter in your own regex statement\n" \
            "9.) Reset log selection to all logs.\n" \
            "10.) Exit"

# Set the value of logs to the all_logs table
logs = all_logs

# Beginning of Menu
while True:
    print(menu_options)

    try:
        user_choice = int(input("Please select one of the above choices: "))
    except ValueError:
        print("Please enter in a valid integer\n")
        continue

    # Print all logs
    if user_choice == 1:
        for log in logs:
            print(log)

    # Search based on log level
    elif user_choice == 2:
        searchtext = str(input("Please enter the string you want to search: "))

        print("You can search for your filter text in the following locations")
        print("1.) Beginning\n2.) End\n3.) Anywhere")
        try:
            location = int(input("Select one of the above options: "))
        except ValueError:
            print("Please enter in a valid integer\n")
            continue

        if location == 1:
            pattern = '^' + searchtext + '.+'
        elif location == 2:
            pattern = '^.+' + searchtext + ',.+'
        elif location == 3:
            pattern = "^.*" + searchtext + ".*,"
        else:
            print("No valid location option selected returning to menu")
            continue

        logs = match_handle(logs, pattern)

    # Search based on log date
    elif user_choice == 3:
        print("Please use the mm/dd/yyyy format for dates.")
        print("Ex. 4/1/2020 | Ex. 12/21/1970")
        date = str(input("Enter the desired date: "))

        pattern = "(.+,){1}" + date + ".*(,.+){4}"
        logs = match_handle(logs, pattern)

    # Search based on log Source
    elif user_choice == 4:

        # Prompt user to input the text they want to search for.
        searchtext = str(input("Please enter the string you want to search: "))

        # Print out a list of all places text can be searched for.
        print("You can search for your filter text in the following locations")
        print("1.) Beginning\n2.) End\n3.) Anywhere")

        # Try to take user input and catch any misinputs/
        try:
            location = int(input("Select one of the above options: "))
        except ValueError:
            print("Please enter in a valid integer\n")
            continue

        # Determine which regex expression to use basd on the user input.
        if location == 1:
            pattern = '^(?:(?:[\w:\/ -])+,){2}' + searchtext
        elif location == 2:
            pattern = '^(?:(?:[\w:\/ -])+,){2}[\w-]*' + searchtext + ','
        elif location == 3:
            pattern = '^(?:(?:[\w:\/ -])+,){2}[\w-]*' + searchtext + '[\w-]*'
        else:
            print("No valid location option selected returning to menu")
            continue

        # Use the logs.search function to get a list of all matching logs
        logs = match_handle(logs, pattern)

    # Search based on Event ID
    elif user_choice == 5:
        # Prompt user to input the text they want to search for.
        searchtext = str(input("Please enter the string you want to search: "))

        # Print out a list of all places text can be searched for.
        print("You can search for your filter text in the following locations")
        print("1.) Beginning\n2.) End\n3.) Anywhere")

        # Try to take user input and catch any misinputs/
        try:
            location = int(input("Select one of the above options: "))
        except ValueError:
            print("Please enter in a valid integer\n")
            continue

        # Determine which regex expression to use basd on the user input.
        if location == 1:
            pattern = '^(?:(?:[\w:\/ -])+,){3}' + searchtext
        elif location == 2:
            pattern = '^(?:(?:[\w:\/ -])+,){3}[\w-]*' + searchtext + ','
        elif location == 3:
            pattern = '^(?:(?:[\w:\/ -])+,){3}[\w-]*' + searchtext + '[\w-]*'
        else:
            print("No valid location option selected returning to menu")
            continue

        logs = match_handle(logs, pattern)

    # Search based on Task Category
    elif user_choice == 6:
        # Prompt user to input the text they want to search for.
        searchtext = str(input("Please enter the string you want to search: "))

        # Print out a list of all places text can be searched for.
        print("You can search for your filter text in the following locations")
        print("1.) Beginning\n2.) End\n3.) Anywhere")

        # Try to take user input and catch any misinputs/
        try:
            location = int(input("Select one of the above options: "))
        except ValueError:
            print("Please enter in a valid integer\n")
            continue

        # Determine which regex expression to use basd on the user input.
        if location == 1:
            pattern = '^(?:(?:[\w:\/ -])+,){4}' + searchtext
        elif location == 2:
            pattern = '^(?:(?:[\w:\/ -])+,){4}[\w-]*' + searchtext + ','
        elif location == 3:
            pattern = '^(?:(?:[\w:\/ -])+,){4}[\w-]*' + searchtext + '[\w-]*'
        else:
            print("No valid location option selected returning to menu")
            continue

        logs = match_handle(logs, pattern)

    # Search based on Description
    elif user_choice == 7:
        # Prompt user to input the text they want to search for.
        searchtext = str(input("Please enter the string you want to search: "))

        # Print out a list of all places text can be searched for.
        print("You can search for your filter text in the following locations")
        print("1.) Beginning\n2.) End\n3.) Anywhere")

        # Try to take user input and catch any misinputs/
        try:
            location = int(input("Select one of the above options: "))
        except ValueError:
            print("Please enter in a valid integer\n")
            continue

        # Determine which regex expression to use basd on the user input.
        if location == 1:
            pattern = '^(?:(?:[\w:\/ -])+,){5}' + searchtext
        elif location == 2:
            pattern = searchtext + '$'
        elif location == 3:
            pattern = '^(?:(?:[\w:\/ -])+,){5}.*' + searchtext + '.*'
        else:
            print("No valid location option selected returning to menu")
            continue

        logs = match_handle(logs, pattern)

    # Custom Regex
    elif user_choice == 8:

        pattern = input("Enter the regex pattern you wish to use: ")

        logs = match_handle(logs, pattern)

    # Refresh the value of logs
    elif user_choice == 9:
        logs = all_logs

    # Quit program
    elif user_choice == 10:
        break

    # If user does not enter a valid option, remind them
    else:
        print("Please enter a number between 1 and 10")
