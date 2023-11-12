import csv
from fuzzywuzzy import fuzz


def handle_university_website(user_input):
    response = ""

    # Read the sports.csv file
    with open('websites.csv', 'r') as file:
        reader = csv.DictReader(file)
        websites = list(reader)

    # Break down user input into individual words
    user_words = user_input.lower().split()

    # Filter sports based on user input words
    filtered_websites = []
    for website in websites:
        website_name = website['website'].lower()
        similarity_score = fuzz.token_set_ratio(user_input, website_name)

        if similarity_score > 90:
            website['similarity_score'] = similarity_score
            filtered_websites.append(website)

    # Sort the matched sports based on similarity score
    filtered_websites = sorted(filtered_websites, key=lambda x: x['similarity_score'], reverse=True)

    # Build the response
    if filtered_websites:
        response += "Yes, here is the requested website:\n"
        for website in filtered_websites:
            response += f"Category: {website['category']}\n"
            response += f"Website: {website['website']}\n"
            response += f"Description: {website['description']}\n\n"
    else:
        response += ("The sport you are searching for is not offered at the university. Please choose from the "
                     "available sports:\n")
        for website in websites:
            response += f"Category: {website['category']}\n"
            response += f"Website: {website['website']}\n"
            response += f"Description: {website['description']}\n\n"

    return response
