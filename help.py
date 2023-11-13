import csv


def handle_help(user_input):
    response = ""

    # Read the help.csv file
    with open('help.csv', 'r') as file:
        reader = csv.DictReader(file)
        help_data = list(reader)

    # Build the response
    if help_data:
        response += "Getting Started:<br><br>"
        for help_item in help_data:
            response += f"Intent: {help_item['Intent']}<br>"
            response += f"Action: {help_item['Action']}<br><br>"
    else:
        response += "No Help Resources were found.<br>"

    return response