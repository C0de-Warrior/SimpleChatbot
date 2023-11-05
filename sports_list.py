import csv


def handle_sports_list(user_input):
    # Read the programs.csv file
    with open('sports.csv', 'r') as file:
        reader = csv.DictReader(file)
        sports = list(reader)

    # Filter programs based on user's specified level
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

    # Print the filtered programs
    if filtered_sports:
        print("Here is a list of available sports:")
        for sport in filtered_sports:
            print(f"Sport: {sport['sport']}")
            print(f"Gender: {sport['gender']}")
            print(f"Description: {sport['description']}")
            print(f"Captain: {sport['captain']}")
            print(f"contact: {sport['contact']}")
            print()
    else:
        print("No sports found.")
