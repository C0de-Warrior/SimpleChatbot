import pandas as pd
import re
from fuzzywuzzy import fuzz

# Load the timetable data from the CSV file
data = pd.read_csv('exams.csv')


def extract_course_code_from_input(user_input):
    # Use regular expression to extract the course code from the user input
    pattern = r'.*?([a-zA-Z]{3}\d{3}).*?'
    match = re.search(pattern, user_input)

    if match:
        course_code = match.group(1).lower()  # Extracted course code in lowercase
        return course_code

    return None  # Return None if no course code is found


def handle_exams_code(user_input):
    print("Input:", user_input)
    course_code = extract_course_code_from_input(user_input)
    print("Course code extracted:", course_code)

    if course_code:
        close_matches = []

        for index, row in data.iterrows():
            row_code = str(row['code'])
            if pd.notnull(row_code):
                similarity = fuzz.token_set_ratio(course_code, row_code.lower())
                if similarity >= 85:
                    close_matches.append(row)

        if close_matches:
            response = "Timetable for the specified course code:<br><br>"
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
            return ("No timetable found for the specified course code. Please retry your question using one of the "
                    "following formats:<br>1. I want to search for an Exam in the Exams Time Table by the ["
                    "course_code] course"
                    "code<br>2. I want to search for the [course_code] course code in the exams Time Table")

    return ("Invalid input format. Please retry your question using one of the following formats:<br>1. I want to "
            "search"
            "for an Exam in the Exams Time Table by the [course_code] course code<br>2. I want to search for the ["
            "course_code] course code in the exams Time Table")


