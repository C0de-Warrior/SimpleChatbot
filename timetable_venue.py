import re
from difflib import SequenceMatcher
import pandas as pd


def get_program_list():
    data = pd.read_csv('time table.csv')
    program_list = data['program'].unique()
    return program_list


def extract_venue_from_input(user_input):
    pattern = r"(?:Can you provide|I want) the timetable for the ([\w\s]+) venue"
    match = re.search(pattern, user_input, re.IGNORECASE)

    if match:
        venue = match.group(1).lower()  # Extracted venue in lowercase
        return venue

    return None


def handle_timetable_venue(query):
    venue = extract_venue_from_input(query)

    if venue:
        timetable = search_timetable_by_venue(venue)
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
                response += f"Lecturer: {row['Lecturer']}<br>"
                response += f"Year: {row['year']}<br>"
                response += f"Program: {row['program']}<br><br>"
            return response

    return "Please provide the venue you want to search for in one of the following formats:<br>" \
           "- Can you provide the timetable for the [Venue] venue<br>" \
           "- I want the timetable for the [Venue] venue"


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
