import pandas as pd
from datetime import datetime
from difflib import SequenceMatcher
import re

# Load the calendar data from the CSV file
data = pd.read_csv('calendar.csv')


def handle_calendar_event(user_input):
    event = extract_event_from_input(user_input)
    if event:
        result = search_events(event)
        if result:
            return result
        else:
            return (f"No events found for '{event}' in the calendar. Please try a different search term or refine your "
                    f"query.")
    else:
        return "Invalid input format. Please retry your question using one of the following formats:\n" \
               "1. 'When is [event] in the Africa University Calendar'\n" \
               "2. 'When is [event] in the school University Calendar'\n" \
               "3. 'I want to search for [event] in the school calendar'"


def extract_event_from_input(user_input):
    # Use regular expression to extract the event from the user input
    pattern1 = r"When is (.*?) in the .*? Calendar"
    pattern2 = r"I want to search for (.*?) in the .*? calendar"
    match1 = re.search(pattern1, user_input, re.IGNORECASE)
    match2 = re.search(pattern2, user_input, re.IGNORECASE)

    if match1:
        event = match1.group(1)
        return event.lower()
    elif match2:
        event = match2.group(1)
        return event.lower()

    return None


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

    return "No events found in the calendar."
