import re
from difflib import SequenceMatcher
import pandas as pd


def get_program_list():
    data = pd.read_csv('time table.csv')
    program_list = data['program'].unique()
    return program_list


def search_timetable_by_program(program, year):
    data = pd.read_csv('time table.csv')
    close_matches = []

    for index, row in data.iterrows():
        row_program = str(row['program'])
        if pd.notnull(row_program):
            similarity = SequenceMatcher(None, program, row_program).ratio()
            if similarity >= 0.85 and year == str(row['year']):  # Convert year to string
                close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable.drop(['year', 'program'], axis=1)

    return "No timetable found for the specified program and year."


def extract_program_year_from_input(user_input):
    pattern = r"I want to search for the year ([\d.]+), ([\w\s]+)\s*program in the school\s*time\s*table"
    match = re.search(pattern, user_input, re.IGNORECASE)

    if match:
        year = match.group(1)  # Extracted year
        program = match.group(2).lower()  # Extracted program in lowercase
        return program, year

    # Fuzzy matching to handle slight variances in program names
    program_list = get_program_list()
    user_program = user_input.lower()
    best_match = None
    best_similarity = 0

    for program in program_list:
        similarity = SequenceMatcher(None, user_program, program.lower()).ratio()
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = program

    if best_match and best_similarity >= 0.85:
        year_pattern = r"I want to search for the year ([\d.]+)\s*program in the school\s*time\s*table"
        year_match = re.search(year_pattern, user_input, re.IGNORECASE)
        if year_match:
            year = year_match.group(1)
            return best_match, year

    return None, None


def handle_timetable_program(query):
    program, year = extract_program_year_from_input(query)

    if program and year:
        timetable = search_timetable_by_program(program, year)
        if isinstance(timetable, str):
            return timetable
        else:
            response = ""
            for _, row in timetable.iterrows():
                response += f"Course Code: {row['Course Code']}<br>"
                response += f"Course Name: {row['Course Name']}<br>"
                response += f"Section: {row['Section']}<br>"
                response += f"Day: {row['Day']}<br>"
                response += f"From Time: {row['From Time']}<br>"
                response += f"To Time: {row['To Time']}<br>"
                response += f"Venue: {row['Venue']}<br>"
                response += f"Lecturer: {row['Lecturer']}<br><br>"
            return response

    return "Please provide the program and year you want to search for in one of the following formats:<br>" \
           "- I want to search for the year [Year], [Program] program in the school time table"
