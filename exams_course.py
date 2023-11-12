import pandas as pd
import re
from fuzzywuzzy import fuzz

# Load the timetable data from the CSV file
data = pd.read_csv('exams.csv')


def extract_course_from_input(user_input):
    # Use regular expression to extract the course name from the user input
    patterns = [
        r'I want to search for the (.*?) course in the exams Time Table',
        r'I want to search for the (.*?) course in the exams timetable',
        r'I want to search for the (.*?) course in the exams',
        r'I want to search for the (.*?) course in the timetable',
        r'I want to search for the (.*?) course',
    ]

    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            course = match.group(1).lower()  # Extracted course name in lowercase
            return course

    return None  # Return None if no course name is found


def handle_exams_course(user_input):
    print("Input:", user_input)
    course = extract_course_from_input(user_input)
    print("Course extracted:", course)

    if course:
        close_matches = []

        for index, row in data.iterrows():
            row_course = str(row['course'])
            if pd.notnull(row_course):
                similarity = fuzz.token_set_ratio(course, row_course.lower())
                if similarity >= 85:
                    close_matches.append(row)

        if close_matches:
            response = "Timetable for the specified course:<br><br>"
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
            return (f"No timetable found for the specified course '{course}'. Please retry your question using one of "
                    f"the following formats:<br>1. I want to search for an Exam in the Exams Time Table by the [{course}] course<br>"
                    f"2. I want to search for the [{course}] course in the exams Time Table")

    return ("Invalid input format. Please retry your question using one of the following formats:<br>1. I want to "
            "search for an Exam in the Exams Time Table by the [course_name] course<br>2. I want to search for the ["
            "course_name] course in the exams Time Table")
