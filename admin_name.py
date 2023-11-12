import pandas as pd
from difflib import SequenceMatcher
import re

# Load the admin data from the CSV file
data = pd.read_csv('admin.csv')

# Define the responsibilities list
responsibilities = [
    "payment plans",
    "fee statement",
    "registration",
    "scholarships",
    "refunds",
    "cashier",
    "invoices"
]


def search_admin_by_name(name):
    close_matches = []
    for index, row in data.iterrows():
        row_name = str(row['name']).lower()
        if pd.notnull(row_name):
            similarity = SequenceMatcher(None, name, row_name).ratio()
            if similarity >= 0.85:
                close_matches.append(row)

    if close_matches:
        admin_data = pd.DataFrame(close_matches)
        return admin_data

    return "No matching records found for the specified name."


def search_admin_by_responsibility(responsibility):
    if responsibility.lower() not in responsibilities:
        return "Invalid responsibility. Please choose from the provided options."

    matches = data[data['responsibility'].str.lower() == responsibility.lower()]
    if not matches.empty:
        return matches

    return "No matching records found for the specified responsibility."


def extract_name_from_input(user_input):
    # Use regular expression to extract the name from the user input
    pattern1 = r'I want the contact details of (.*?) from the Administrator office'
    pattern2 = r'I want to search for the contact details of (.*?) from the administrators office'
    match1 = re.search(pattern1, user_input)
    match2 = re.search(pattern2, user_input)

    if match1:
        name = match1.group(1).lower()  # Extracted name in lowercase
        return name
    elif match2:
        name = match2.group(1).lower()  # Extracted name in lowercase
        return name

    return None  # Return None if no name is found


def handle_admin_name(user_input):
    name = extract_name_from_input(user_input)
    if name:
        admin_data = search_admin_by_name(name)
        if isinstance(admin_data, pd.DataFrame):
            # Format the data for neat and clear display
            response = ""
            for _, row in admin_data.iterrows():
                response += f"Name: {row['name']}<br>"
                response += f"Responsibility: {row['responsibility']}<br>"
                response += f"Extension: {row['ext']}<br>"
                response += f"Email: {row['email']}<br>"
                response += f"Work Hours: {row['work hours']}<br><br>"
            return response.strip()  # Remove trailing whitespace
        else:
            return admin_data
    else:
        response = "Invalid input format. Please retry your question using one of the following formats:<br>" \
                   "1. 'I want the contact details of [name] from the Administrator office'<br>" \
                   "2. 'I want to search for the contact details of [name] from the administrators office'"
        if 'name' in user_input:
            response += f"<br><br>The searched name '{user_input.split(' ')[-2]}' could not be found. " \
                        f"Please try asking your question with the correct format to potentially improve search results."
        return response