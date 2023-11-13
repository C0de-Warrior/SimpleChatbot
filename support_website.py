import csv


def handle_support_website(category):
    response = ""

    # Read the websites.csv file
    with open('websites.csv', 'r') as file:
        reader = csv.DictReader(file)
        websites = list(reader)

    category = "support"
    # Filter websites based on the category variable
    filtered_websites = [website for website in websites if website['category'].lower() == category.lower()]

    # Build the response
    if filtered_websites:
        response += "Yes, here is the website you require:<br><br>"
        for website in filtered_websites:
            response += f"Category: {website['category']}<br>"
            response += f"Website: {website['website']}<br>"
            response += f"Description: {website['description']}<br><br>"
    else:
        response += "No websites found in the requested category.<br>"

    return response
