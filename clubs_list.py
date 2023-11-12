import csv


def handle_clubs_list(user_input):
    # Read the clubs.csv file
    with open('clubs.csv', 'r') as file:
        reader = csv.DictReader(file)
        clubs = list(reader)

    # Generate the response
    response = ""
    if clubs:
        response += "Here is a list of available clubs:<br><br>"
        for club in clubs:
            response += f"Club: {club['club']}<br>"
            response += f"Description: {club['description']}<br><br>"
    else:
        response = "No clubs found."

    return response