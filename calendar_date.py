import pandas as pd
from datetime import datetime
import re

# Load the calendar data from the CSV file
data = pd.read_csv('calendar.csv')


def handle_calendar_date(user_input):
    if user_input.lower() == "exit":
        return False

    event_date = extract_date_from_input(user_input)
    if event_date:
        result = search_events(event_date)
        if result:
            return result
        else:
            return f"No events found for {event_date} in the calendar. Please try a different date or refine your query."
    else:
        return "Invalid input format. Please retry your question using one of the following formats:\n" \
               "1. 'What events are on [date] in the school Calendar'"


def extract_date_from_input(user_input):
    # Use regular expression to extract the date from the user input
    pattern = r"What events are on (.*?) in the .*? Calendar"
    match = re.search(pattern, user_input, re.IGNORECASE)  # Add re.IGNORECASE flag to match case-insensitively

    if match:
        event_date = match.group(1)
        try:
            parsed_date = datetime.strptime(event_date, "%d-%b-%y")
            return parsed_date.date()
        except ValueError:
            return None

    return None


def search_events(query_date):
    formatted_query_date = query_date.strftime("%d-%b-%y")
    results = data[data['date'] == formatted_query_date]
    if not results.empty:
        return results[['date', 'event']].to_string(index=False)
    else:
        return f"No events found on {formatted_query_date}."
