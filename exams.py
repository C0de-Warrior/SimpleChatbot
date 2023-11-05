import pandas as pd
from difflib import SequenceMatcher

# Load the timetable data from the CSV file
data = pd.read_csv('exams.csv')


def search_timetable_by_course_title(course_title):
    close_matches = []
    for index, row in data.iterrows():
        row_course_title = str(row['course'])
        if pd.notnull(row_course_title):
            similarity = SequenceMatcher(None, course_title, row_course_title).ratio()
            if similarity >= 0.85:
                close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable

    return "No timetable found for the specified course title."


def search_timetable_by_venue(venue):
    close_matches = []
    for index, row in data.iterrows():
        row_venue = str(row['venue'])
        if pd.notnull(row_venue):
            similarity = SequenceMatcher(None, venue, row_venue).ratio()
            if similarity >= 0.85:
                close_matches.append(row)

    if close_matches:
        timetable = pd.DataFrame(close_matches)
        return timetable

    return "No timetable found for the specified venue."


def search_timetable_by_course_code(course_code):
    matches = data[data['code'] == course_code]
    if not matches.empty:
        return matches

    return "No timetable found for the specified course code."


def handle_exams(user_input):
    user_input = input(
        "Please select an option:\n1. Search for timetable by course title\n2. Search for timetable by venue\n3. Search for timetable by course code\nYour choice: ").lower()
    if user_input == "1":
        course_title = input("Enter the course title: ").lower()
        timetable = search_timetable_by_course_title(course_title)
        print(timetable)
    elif user_input == "2":
        venue = input("Enter the venue: ").lower()
        timetable = search_timetable_by_venue(venue)
        print(timetable)
    elif user_input == "3":
        course_code = input("Enter the course code: ").lower()
        timetable = search_timetable_by_course_code(course_code)
        print(timetable)
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


# Example usage
