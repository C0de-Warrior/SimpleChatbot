import pandas as pd
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
import re

# Load the admin data from the CSV file
data = pd.read_excel('admin.xls')

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
    matches = []
    for resp in data['responsibility']:
        similarity = fuzz.token_set_ratio(responsibility.lower(), resp.lower())
        if similarity >= 80:
            matches.append(resp)

    if matches:
        filtered_data = data[data['responsibility'].apply(lambda x: any(m.lower() in x.lower() for m in matches))]
        if not filtered_data.empty:
            response = ""
            for _, row in filtered_data.iterrows():
                response += f"Name: {row['name']}<br>"
                response += f"Responsibility: {row['responsibility']}<br>"
                response += f"Extension: {row['ext']}<br>"
                response += f"Email: {row['email']}<br>"
                response += f"Work Hours: {row['work hours']}<br><br>"
            return response

    return "No matching records found for the specified responsibility."


def extract_responsibility_from_input(user_input):
    # Use regular expression to extract the responsibility from the user input
    patterns = [
        r'I want the contact details of the person at the Administrator office who is in charge of (.*?)$',
        r'I want the contact details of the person at the Administrator office whose in charge of (.*?)$',
        r'I want the contact details of the person at the Administrator office who is in responsible (.*?)$',
        r'I want the contact details of the person at the Administrator office whose role is (.*?)$',
        r'Who is responsible for (.*?) at the Administrator office$',
        r'Whose role is (.*?) at the Administrator office$'
    ]

    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            responsibility = match.group(1).lower()  # Extracted responsibility in lowercase
            return responsibility

    return None  # Return None if no responsibility is found


def handle_admin_role(user_input):
    responsibility = extract_responsibility_from_input(user_input)
    if responsibility:
        admin_data = search_admin_by_responsibility(responsibility)
        if isinstance(admin_data, pd.DataFrame):
            return str(admin_data)
        else:
            return admin_data
    else:
        response = "Invalid input format. Please retry your question using one of the following formats:\n" \
                   "1. 'I want the contact details of the person at the Administrator office who is in charge of [responsibility]'\n" \
                   "2. 'I want the contact details of the person at the Administrator office whose in charge of [responsibility]'\n" \
                   "3. 'I want the contact details of the person at the Administrator office who is in responsible [responsibility]'\n" \
                   "4. 'I want the contact details of the person at the Administrator office whose role is [responsibility]'\n" \
                   "5. 'Who is responsible for [responsibility] at the Administrator office'\n" \
                   "6. 'Whose role is [responsibility] at the Administrator office'"

        if responsibility:
            response += f"\n\nThe searched responsibility '{responsibility}' could not be found. " \
                        f"Please try asking your question with the correct format or choose from the following responsibilities: {', '.join(responsibilities)}"
        return response


