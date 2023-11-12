import pandas as pd
from datetime import datetime
from difflib import SequenceMatcher


def handle_calendar(user_input):
    if user_input.lower() == "exit":
        return False

    if user_input == "1":
        event_query = input("Enter the event you want to search: ")
        result = search_events(event_query)
        return result
    elif user_input == "2":
        return "Please enter the date in the format 'DD-Mon-YY'"
    else:
        return "Invalid choice. Please enter 1 or 2."


def search_events(query):
    today = datetime.today().date()
    query_date = None

    try:
        query_date = datetime.strptime(query, "%d-%b-%y").date()
    except ValueError:
        pass

    if query_date:
        if query_date < today:
            return "The specified date has already passed."

        results = data[data['date'] == query_date]
        if not results.empty:
            return results[['date', 'event']].to_string(index=False)
        else:
            return "No events found on the specified date."
    else:
        exact_match = data[data['event'] == query]
        if not exact_match.empty:
            return exact_match[['date', 'event']].to_string(index=False)

        close_matches = []
        for event in data['event']:
            similarity = SequenceMatcher(None, query, event).ratio()
            if similarity >= 0.5:
                close_matches.append(event)

        if close_matches:
            return f"Event not found. Did you mean:\n{', '.join(close_matches)}"

    return "No events found."


# Load the calendar data from the CSV file
data = pd.read_csv('calendar.csv')