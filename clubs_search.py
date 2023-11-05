import csv


def handle_clubs_search(user_input):
    # Read the sports.csv file
    with open('clubs.csv', 'r') as file:
        reader = csv.DictReader(file)
        clubs = list(reader)

    # Break down user input into individual words
    user_words = user_input.lower().split()

    # Initialize gender variable
    # gender = ''

    # Filter sports based on user's specified gender
    # if 'mens' in user_input:
    #     gender = 'mens'
    # elif 'womens' in user_input:
    #     gender = 'womens'
    # elif 'mixed' in user_input:
    #     gender = 'mixed'

    # Filter sports based on user input words and gender
    filtered_clubs = []
    for club in clubs:
        club_words = club['club'].lower().split()
        if any(word in club_words for word in user_words):
            filtered_clubs.append(club)

    # Print the filtered sports
    if filtered_clubs:
        print("Here is a list of available clubs:")
        for club in filtered_clubs:
            print(f"Club: {club['club']}")
            print(f"Description: {club['description']}")
            print()
    else:
        print(
            "The club you are searching for is not offered at the university. Please choose from the available sports:")
        for club in filtered_clubs:
            print(f"Club: {club['club']}")
            print(f"Description: {club['description']}")
            print()