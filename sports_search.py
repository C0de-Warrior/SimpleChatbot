import csv
from fuzzywuzzy import fuzz


def handle_sports_search(user_input):
    # Read the sports.csv file
    with open('sports.csv', 'r') as file:
        reader = csv.DictReader(file)
        sports = list(reader)

    # Break down user input into individual words
    user_words = user_input.lower().split()

    # Initialize gender variable
    gender = ''

    # Check user input for gender keywords
    if any(word in user_input for word in ['girls', 'womens', 'women']):
        gender = 'womens'
    elif any(word in user_input for word in ['mens', 'men', 'boys']):
        gender = 'mens'
    elif any(word in user_input for word in ['mixed', 'combined']):
        gender = 'mixed'

    # Filter sports based on user input words and gender
    filtered_sports = []
    for sport in sports:
        sport_name = sport['sport'].lower()
        similarity_score = fuzz.token_set_ratio(user_input, sport_name)

        if similarity_score > 90 and (gender == '' or sport['gender'] == gender):
            sport['similarity_score'] = similarity_score
            filtered_sports.append(sport)

    # Sort the matched sports based on similarity score
    filtered_sports = sorted(filtered_sports, key=lambda x: x['similarity_score'], reverse=True)

    # Print the filtered sports
    if filtered_sports:
        print("Yes, here is a list of available sports:")
        for sport in filtered_sports:
            print(f"Sport: {sport['sport']}")
            print(f"Gender: {sport['gender']}")
            print(f"Description: {sport['description']}")
            print(f"Captain: {sport['captain']}")
            print(f"Contact: {sport['contact']}")
            print()
    else:
        print("The sport you are searching for is not offered at the university. Please choose from the available "
              "sports:")
        for sport in sports:
            if gender == '' or sport['gender'] == gender:
                print(f"Sport: {sport['sport']}")
                print(f"Gender: {sport['gender']}")
                print(f"Description: {sport['description']}")
                print(f"Captain: {sport['captain']}")
                print(f"Contact: {sport['contact']}")
                print()
