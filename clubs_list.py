import csv


def handle_clubs_list(user_input):
    # Read the programs.csv file
    with open('clubs.csv', 'r') as file:
        reader = csv.DictReader(file)
        clubs = list(reader)

    # Filter programs based on user's specified level
    # gender = ''
    # user_input = user_input.lower()

    # if 'mens' in user_input:
    # gender = 'mens'
    # elif 'womens' in user_input:
    # gender = 'womens'
    # elif 'mixed' in user_input:
    # gender = 'mixed'

    # filtered_sports = []
    # for sport in sports:
    #     if gender == '' or sport['gender'].lower() == gender:
    #         filtered_sports.append(sport)

    # Print the clubs
    if clubs:
        print("Here is a list of available clubs:")
        for club in clubs:
            print(f"CLub: {club['club']}")
            print(f"Description: {club['description']}")
            print()
    else:
        print("No club found.")
