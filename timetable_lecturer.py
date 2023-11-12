import re
from difflib import SequenceMatcher
import pandas as pd


def extract_lecturer_from_input(user_input):
    pattern = r"(?:Can you provide|I want) the timetable for ([\w\s]+)"
    match = re.search(pattern, user_input, re.IGNORECASE)

    if match:
        lecturer = match.group(1).lower()  # Extracted lecturer in lowercase
        return lecturer

    return None


def handle_timetable_lecturer(query):
    lecturer = extract_lecturer_from_input(query)

    if lecturer:
        timetable = search_timetable_by_lecturer(lecturer)
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
                response += f"Lecturer: {row['Lecturer']}<br>"
                response += f"Year: {row['year']}<br>"
                response += f"Program: {row['program']}<br><br>"
            return response

    return "Please provide the Lecturer Name you want to search for in one of the following formats:<br>" \
           "- Can you provide the timetable for the [Lecturer]?<br>" \
           "- I want the timetable for the [Lecturer]"


def search_timetable_by_lecturer(lecturer):
    data = pd.read_csv('time table.csv')
    close_matches = []
    for _, row in data.iterrows():
        similarity = SequenceMatcher(None, lecturer, row['Lecturer'].lower()).ratio()
        if similarity >= 0.80:
            close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable.drop(['year', 'program'], axis=1)

    return "No timetable found for the specified lecturer."
