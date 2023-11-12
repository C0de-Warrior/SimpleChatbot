import pandas as pd
from difflib import SequenceMatcher

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


def handle_admin(user_input):
    response = ""
    if user_input == "1":
        response += "Enter the name: "
        # Instead of using `input`, you can directly call the `search_admin_by_name` function
        # and append the result to the `response` string
        # Example: response += str(search_admin_by_name(name))
    elif user_input == "2":
        response += "Please choose from the following responsibilities:\n"
        response += "1. Payment Plans\n"
        response += "2. Fee Statement\n"
        response += "3. Registration\n"
        response += "4. Scholarships\n"
        response += "5. Refunds\n"
        response += "6. Cashier\n"
        response += "7. Invoices\n"
        response += "Enter the responsibility choice number: "
        # Instead of using `input`, you can directly call the `search_admin_by_responsibility` function
        # and append the result to the `response` string
        # Example: response += str(search_admin_by_responsibility(responsibility))
    else:
        response = "Invalid choice. Please enter 1 or 2."

    return response
