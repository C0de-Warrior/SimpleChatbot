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
    user_input = input(
        "Please select an option:\n1. Search for admin by name\n2. Search for admin by responsibility\nYour choice: ")

    if user_input == "1":
        name = input("Enter the name: ").lower()
        admin_data = search_admin_by_name(name)
        print(admin_data)
    elif user_input == "2":
        print("Please choose from the following responsibilities:")
        print("1. Payment Plans")
        print("2. Fee Statement")
        print("3. Registration")
        print("4. Scholarships")
        print("5. Refunds")
        print("6. Cashier")
        print("7. Invoices")
        responsibility_choice = input("Enter the responsibility choice number: ")

        if responsibility_choice == "1":
            responsibility = "payment plans"
        elif responsibility_choice == "2":
            responsibility = "fee statement"
        elif responsibility_choice == "3":
            responsibility = "registration"
        elif responsibility_choice == "4":
            responsibility = "scholarships"
        elif responsibility_choice == "5":
            responsibility = "refunds"
        elif responsibility_choice == "6":
            responsibility = "cashier"
        elif responsibility_choice == "7":
            responsibility = "invoices"
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            return

        # Convert the responsibility choice to lowercase for comparison
        responsibility_choice_lower = responsibility_choice.lower()

        # Check if the lowercase responsibility choice is in the lowercase responsibilities list
        if responsibility_choice_lower in [r.lower() for r in responsibilities]:
            admin_data = search_admin_by_responsibility(responsibility)
            print(admin_data)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            return

        admin_data = search_admin_by_responsibility(responsibility)
        print(admin_data)
    else:
        print("Invalid choice. Please enter 1 or 2.")