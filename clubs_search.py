import csv


def handle_clubs_search(user_input):
    # Read the clubs.csv file
    with open('clubs.csv', 'r') as file:
        reader = csv.DictReader(file)
        clubs = list(reader)

    # Break down user input into individual words
    user_words = user_input.lower().split()

    # Filter clubs based on user input words
    filtered_clubs = []
    for club in clubs:
        club_words = club['club'].lower().split()
        if any(word in club_words for word in user_words):
            filtered_clubs.append(club)

    # Generate the response
    response = ""
    if filtered_clubs:
        response += "Here is a list of available clubs:<br><br>"
        for club in filtered_clubs:
            response += f"Club: {club['club']}<br>"
            response += f"Description: {club['description']}<br><br>"
    else:
        response = ("The club you are searching for is not offered at the university. Please choose from the available "
                    "clubs.")

    return response