import csv

def handle_sports_list(user_input):
    response = ""

    # Read the sports.csv file
    with open('sports.csv', 'r') as file:
        reader = csv.DictReader(file)
        sports = list(reader)

    # Filter sports based on user's specified gender
    gender = ''
    user_input = user_input.lower()

    if 'mens' in user_input:
        gender = 'mens'
    elif 'womens' in user_input:
        gender = 'womens'
    elif 'mixed' in user_input:
        gender = 'mixed'

    filtered_sports = []
    for sport in sports:
        if gender == '' or sport['gender'].lower() == gender:
            filtered_sports.append(sport)

    # Prepare the response
    if filtered_sports:
        response += "Here is a list of available sports:<br><br>"
        for sport in filtered_sports:
            response += f"Sport: {sport['sport']}<br>"
            response += f"Gender: {sport['gender']}<br>"
            response += f"Description: {sport['description']}<br>"
            response += f"Captain: {sport['captain']}<br>"
            response += f"Contact: {sport['contact']}<br><br>"
    else:
        response += "No sports found."

    return response