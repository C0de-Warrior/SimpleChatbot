import pandas as pd
from difflib import SequenceMatcher


def search_timetable_by_program(program, year):
    data = pd.read_csv('time table.csv')
    close_matches = []
    for index, row in data.iterrows():
        row_program = str(row['program'])
        if pd.notnull(row_program):
            similarity = SequenceMatcher(None, program, row_program).ratio()
            if similarity >= 0.85 and year == row['year']:
                close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable.drop(['year', 'program'], axis=1)

    return "No timetable found for the specified program and year."


def search_timetable_by_venue(venue):
    data = pd.read_csv('time table.csv')
    close_matches = []
    for index, row in data.iterrows():
        similarity = SequenceMatcher(None, venue, row['Venue']).ratio()
        if similarity >= 0.85:
            close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable.drop(['year', 'program'], axis=1)

    return "No timetable found for the specified venue."


def search_timetable_by_lecturer(lecturer):
    data = pd.read_csv('time table.csv')
    close_matches = []
    for index, row in data.iterrows():
        similarity = SequenceMatcher(None, lecturer, row['Lecturer']).ratio()
        if similarity >= 0.85:
            close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable.drop(['year', 'program'], axis=1)

    return "No timetable found for the specified lecturer."


def get_program_list():
    data = pd.read_csv('time table.csv')
    program_list = data['program'].unique()
    return program_list


def handle_timetable():
    response = "Please select an option:\n"
    response += "1. Search for timetable by program\n"
    response += "2. Search for timetable by venue\n"
    response += "3. Search for timetable by lecturer\n"
    response += "4. Get program list\n"
    response += "Enter 'exit' to quit\n"

    user_input = input("Your choice: ")

    if user_input.lower() == "exit":
        return response

    if user_input == "1":
        program = input("Enter the program: ")

        year_options = {
            "1": 1.1,
            "2": 1.2,
            "3": 2.1,
            "4": 2.2,
            "5": 3.1,
            "6": 4.1
        }

        response += "Select a year:\n"
        for option, year in year_options.items():
            response += f"{option}. {year}\n"

        choice = input("Enter your choice: ")

        if choice in year_options:
            year = year_options[choice]
            timetable = search_timetable_by_program(str(program), year)  # Convert program to string
            response += str(timetable) + "\n"
        else:
            response += "Invalid choice. Please select a valid option.\n"
    elif user_input == "2":
        venue = input("Enter the venue: ")
        timetable = search_timetable_by_venue(venue)
        response += str(timetable) + "\n"
    elif user_input == "3":
        lecturer = input("Enter the lecturer: ")
        timetable = search_timetable_by_lecturer(lecturer)
        response += str(timetable) + "\n"
    elif user_input == "4":
        program_list = get_program_list()
        response += str(program_list) + "\n"
    else:
        response += "Invalid choice. Please enter a number between 1 and 4.\n"

    return response
