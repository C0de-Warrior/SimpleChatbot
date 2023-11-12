import pandas as pd
import re
from fuzzywuzzy import fuzz

# Load the timetable data from the CSV file
data = pd.read_csv('exams.csv')


def extract_venue_from_input(user_input):
    # Use regular expression to extract the venue from the user input
    pattern1 = r'I want to search for an Exam in the Exams Time Table by the (.*?) venue'
    pattern2 = r'I want to search for the (.*?)venue in the exams Time Table'

    match1 = re.search(pattern1, user_input)
    match2 = re.search(pattern2, user_input)

    if match1:
        venue = match1.group(1).lower()  # Extracted venue in lowercase
        return venue
    elif match2:
        venue = match2.group(1).lower()  # Extracted venue in lowercase
        return venue

    return None  # Return None if no venue is found


def extract_venue_from_input(user_input):
    # Use regular expression to extract the venue from the user input
    patterns = [
        r'I want to search for an Exam in the Exams Time Table by the (.*?) venue',
        r'I want to search for an Exam in the Exams TimeTable by the (.*?) venue',
        r'I want to search for the (.*?)venue in the exams Time Table',
        r'I want to search for the (.*?)venue in the exams TimeTable',
        r'I want to search for an Exam in the Exams Time Table by the (.*?)venue',
        r'I want to search for an Exam in the Exams TimeTable by the (.*?)venue',
    ]

    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            venue = match.group(1).lower()  # Extracted venue in lowercase
            return venue

    return None  # Return None if no venue is found


def handle_exams_venue(user_input):
    print("Input:", user_input)
    venue = extract_venue_from_input(user_input)
    print("Venue extracted:", venue)

    if venue:
        close_matches = []

        for index, row in data.iterrows():
            row_venue = str(row['venue'])
            if pd.notnull(row_venue):
                similarity = fuzz.token_set_ratio(venue, row_venue)
                if similarity >= 85:
                    close_matches.append(row)

        if close_matches:
            response = "Timetable for the specified venue:<br><br>"
            for match in close_matches:
                response += f"Date: {match['date']}<br>"
                response += f"Start Time: {match['start time']}<br>"
                response += f"End Time: {match['end time']}<br>"
                response += f"College: {match['college']}<br>"
                response += f"Code: {match['code']}<br>"
                response += f"Course: {match['course']}<br>"
                response += f"No: {match['no']}<br>"
                response += f"Location: {match['location']}<br>"
                response += f"Venue: {match['venue']}<br><br>"
            return response
        else:
            return f"No timetable found for the specified venue '{venue}'. Please retry your question using one of the following formats:<br>1. I want to search for an Exam in the Exams Time Table by the [{venue}] venue<br>2. I want to search for the [{venue}]venue in the exams Time Table"

    return "Invalid input format. Please retry your question using one of the following formats:<br>1. I want to search for an Exam in the Exams Time Table by the [venue_name] venue<br>2. I want to search for the [venue_name]venue in the exams Time Table"
